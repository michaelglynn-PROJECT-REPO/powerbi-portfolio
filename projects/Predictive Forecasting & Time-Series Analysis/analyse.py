# ---Imports---
import math
import numpy as np
import pandas as pd
from pathlib import Path
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="statsmodels")

# ---Config---
INPUT_CSV  = "project3_monthly_metrics.csv"
OUT_BEST   = "project3_monthly_forecast.csv"
OUT_ALL    = "project3_model_forecasts.csv"
OUT_METR   = "project3_model_metrics.csv"
H          = 12
TEST_SIZE  = 12
SEASONAL_PERIODS = 12

# ---Helpers---
def academic_year(d: pd.Timestamp) -> str:
    return f"{d.year}/{str(d.year+1)[2:]}" if d.month >= 8 else f"{d.year-1}/{str(d.year)[2:]}"
def scale_series(y: pd.Series):
    s = y.dropna()
    if s.empty: return y, 1.0
    k = np.nanmedian(s); 
    if not np.isfinite(k) or k == 0: k = max(1.0, np.nanmean(s))
    return y / k, float(k)
def make_positive(y: pd.Series):
    m = y.min(); shift = 0.0
    if pd.notna(m) and m <= 0: shift = 1 - m
    return y + shift, shift
def seasonal_naive(y: pd.Series, idx: pd.DatetimeIndex) -> pd.Series:
    return pd.Series([(y[d - pd.DateOffset(years=1)] if (d - pd.DateOffset(years=1)) in y.index else y.iloc[-1]) for d in idx], index=idx, dtype="float64")
def adf_stats(y: pd.Series):
    s = y.dropna()
    if len(s) < 15: return (np.nan, np.nan)
    try:
        stat, p, *_ = adfuller(s, autolag="AIC"); return float(stat), float(p)
    except Exception:
        return (np.nan, np.nan)
def horizon_to_end_next_ay(last_actual: pd.Timestamp):
    start = last_actual + pd.offsets.MonthBegin(1)
    ay_start_year = start.year if start.month >= 9 else start.year - 1
    end = pd.Timestamp(year=ay_start_year + 2, month=8, day=1)  # Aug of next AY
    n_months = (end.year - start.year) * 12 + (end.month - start.month) + 1
    return start, int(n_months)

# ---Load & aggregate---
df = pd.read_csv(INPUT_CSV, parse_dates=["MonthStart","MonthEnd"]).sort_values("MonthStart")
monthly = df.groupby("MonthStart")[["Enrolments","Withdrawals","Completions"]].sum().reset_index()
base = monthly.set_index("MonthStart").asfreq("MS")

# ---Fit all ETS combos and forecast---
def evaluate_and_forecast_all(series: pd.Series, target_name: str):
    y_raw = series.copy()
    fc_start, H_dyn = horizon_to_end_next_ay(series.index[-1])
    future_idx = pd.date_range(fc_start, periods=H_dyn, freq="MS")
    combos = [("add","add"), ("add","mul"), ("mul","add"), ("mul","mul")]
    do_cv = series.dropna().shape[0] >= TEST_SIZE + max(2, SEASONAL_PERIODS)

    results = []
    for tr, seas in combos:
        rmse = np.nan; shift = 0.0; scale = 1.0
        y_pos, shift = (make_positive(y_raw) if (tr == "mul" or seas == "mul") else (y_raw, 0.0))
        y_scaled, scale = scale_series(y_pos)

        try:
            # CV RMSE (last TEST_SIZE months)
            if do_cv:
                train = y_scaled.iloc[:-TEST_SIZE]; test = y_scaled.iloc[-TEST_SIZE:]
                fit_cv = ExponentialSmoothing(train, trend=tr, seasonal=seas, seasonal_periods=SEASONAL_PERIODS, initialization_method="estimated").fit()
                pred_bt = fit_cv.forecast(len(test)) * scale
                test_bt = test * scale
                if shift != 0: pred_bt -= shift; test_bt -= shift
                rmse = float(math.sqrt(mean_squared_error(test_bt, pred_bt)))

            # Full fit and forecast
            fit_full = ExponentialSmoothing(y_scaled, trend=tr, seasonal=seas, seasonal_periods=SEASONAL_PERIODS, initialization_method="estimated").fit()
            fc = fit_full.forecast(H_dyn) * scale
            fitted = fit_full.fittedvalues * scale
            if shift != 0: fc -= shift; fitted -= shift

            # RMSE fallback from fitted tail
            if not np.isfinite(rmse):
                actual = y_raw.reindex(fitted.index)
                tail = min(TEST_SIZE, int(actual.dropna().shape[0]))
                if tail >= 2:
                    rmse = float(np.sqrt(((actual.iloc[-tail:] - fitted.iloc[-tail:]) ** 2).mean()))
                else:
                    rmse = float(np.sqrt(((actual - fitted) ** 2).dropna().mean()))

            fc_series = pd.Series(fc.values, index=future_idx, dtype="float64")

        except Exception:
            fc_series = seasonal_naive(y_raw, future_idx)
            # naive RMSE approx
            tail = min(TEST_SIZE, len(y_raw.dropna()))
            if tail >= 2:
                idx_tail = y_raw.index[-tail:]
                fitted_tail = [y_raw[d - pd.DateOffset(years=1)] if (d - pd.DateOffset(years=1)) in y_raw.index else y_raw.iloc[-2] for d in idx_tail]
                rmse = float(np.sqrt(((y_raw.iloc[-tail:].values - np.array(fitted_tail)) ** 2).mean()))

        results.append({
            "Target": target_name, "Trend": tr, "Seasonal": seas,
            "RMSE": rmse, "ShiftApplied": shift, "ScaleApplied": scale,
            "Forecast": fc_series,
        })

    # choose best by RMSE
    best = min(results, key=lambda r: (not np.isfinite(r["RMSE"]), r["RMSE"]))
    return results, best

# ---Run---
res_enr, best_enr = evaluate_and_forecast_all(base["Enrolments"], "Enrolments")
res_wd,  best_wd  = evaluate_and_forecast_all(base["Withdrawals"], "Withdrawals")

# ---Export best-model train/test splits---
def export_train_test(series: pd.Series, trend: str, seasonal: str, target: str, out_path: Path, test_size: int = TEST_SIZE):
    y_raw = series.asfreq("MS")
    y_pos, shift = (make_positive(y_raw) if (trend == "mul" or seasonal == "mul") else (y_raw, 0.0))
    y_scaled, scale = scale_series(y_pos)
    train = y_scaled.iloc[:-test_size]; test = y_scaled.iloc[-test_size:]
    fit = ExponentialSmoothing(train, trend=trend, seasonal=seasonal, seasonal_periods=SEASONAL_PERIODS, initialization_method="estimated").fit()
    pred_test = fit.forecast(len(test)) * scale
    if shift != 0: pred_test -= shift
    df_train = pd.DataFrame({"MonthStart": train.index, "Target": target, "Partition": "Train", "Actual": y_raw.loc[train.index].values, "Pred": np.nan, "Trend": trend, "Seasonal": seasonal})
    df_test  = pd.DataFrame({"MonthStart": test.index,  "Target": target, "Partition": "Test",  "Actual": y_raw.loc[test.index].values,  "Pred": pred_test.values, "Trend": trend, "Seasonal": seasonal})
    out = pd.concat([df_train, df_test], ignore_index=True)
    out["AcademicYear"] = out["MonthStart"].apply(academic_year)
    out.to_csv(out_path, index=False)

export_train_test(base["Enrolments"],  best_enr["Trend"], best_enr["Seasonal"], "Enrolments",  Path("project3_best_train_test_Enrolments.csv"))
export_train_test(base["Withdrawals"], best_wd["Trend"],  best_wd["Seasonal"],  "Withdrawals", Path("project3_best_train_test_Withdrawals.csv"))

# ---Best-only output (same shape you use in PBI)---
best_fc = pd.DataFrame({
    "MonthStart": best_enr["Forecast"].index,
    "Enrolments": best_enr["Forecast"].values,
    "Withdrawals": best_wd["Forecast"].values,
    "Completions": pd.NA, "IsForecast": 1
})
actuals = base.reset_index().copy(); actuals["IsForecast"] = 0
out_best = pd.concat([actuals, best_fc], ignore_index=True)
out_best["MonthEnd"] = out_best["MonthStart"] + pd.offsets.MonthEnd(0)
out_best["AcademicYear"] = out_best["MonthStart"].apply(academic_year)
out_best.to_csv(OUT_BEST, index=False)

# ---All models long-form (for comparison plots)---
def stack_one(target_name: str, res_list, y_actual: pd.Series):
    frames = []
    for r in res_list:
        a = pd.DataFrame({"MonthStart": y_actual.index, "Target": target_name, "Trend": r["Trend"], "Seasonal": r["Seasonal"], "Kind": "Actual", "Value": y_actual.values})
        f = pd.DataFrame({"MonthStart": r["Forecast"].index, "Target": target_name, "Trend": r["Trend"], "Seasonal": r["Seasonal"], "Kind": "Forecast", "Value": r["Forecast"].values})
        frames.append(pd.concat([a, f], ignore_index=True))
    return pd.concat(frames, ignore_index=True)

all_long = pd.concat([stack_one("Enrolments", res_enr, base["Enrolments"]),
                      stack_one("Withdrawals", res_wd, base["Withdrawals"])], ignore_index=True)
all_long["MonthEnd"] = all_long["MonthStart"] + pd.offsets.MonthEnd(0)
all_long["AcademicYear"] = all_long["MonthStart"].apply(academic_year)
all_long.to_csv(OUT_ALL, index=False)

# ---Metrics (RMSE, NRMSE, ADF)---
def metrics_frame(target_name: str, res_list, series: pd.Series):
    adf_stat, adf_p = adf_stats(series)
    y = series.dropna()
    mean_y  = float(np.nanmean(y)) if len(y) else np.nan
    range_y = float(np.nanmax(y) - np.nanmin(y)) if len(y) else np.nan
    rows = []
    for r in res_list:
        nrmse_mean  = (r["RMSE"] / mean_y)  if (np.isfinite(r["RMSE"]) and mean_y  not in (0, np.nan)) else np.nan
        nrmse_range = (r["RMSE"] / range_y) if (np.isfinite(r["RMSE"]) and range_y not in (0, np.nan)) else np.nan
        rows.append({
            "Target": target_name, "Trend": r["Trend"], "Seasonal": r["Seasonal"],
            "RMSE": r["RMSE"], "NRMSE_Mean": nrmse_mean, "NRMSE_Range": nrmse_range,
            "ADF_Stat": adf_stat, "ADF_PValue": adf_p,
            "ShiftApplied": r["ShiftApplied"], "ScaleApplied": r["ScaleApplied"],
        })
    return pd.DataFrame(rows)

metrics = pd.concat([metrics_frame("Enrolments", res_enr, base["Enrolments"]),
                     metrics_frame("Withdrawals", res_wd, base["Withdrawals"])], ignore_index=True)
metrics.to_csv(OUT_METR, index=False)

# ---Per-model CSVs + clean actuals (for simple PBI plotting)---
OUT_DIR = Path(".")
def fname(target, trend, seasonal): return OUT_DIR / f"project3_forecast_{target}_{trend}-{seasonal}.csv"
def save_series(path, idx, vals, target):
    pd.DataFrame({"MonthStart": idx, "Target": target, "Value": vals, "AcademicYear": [academic_year(d) for d in idx]}).to_csv(path, index=False)

save_series(OUT_DIR / "project3_actuals_Enrolments.csv",  base.index, base["Enrolments"].values,  "Enrolments")
save_series(OUT_DIR / "project3_actuals_Withdrawals.csv", base.index, base["Withdrawals"].values, "Withdrawals")
for res_list, target in [(res_enr, "Enrolments"), (res_wd, "Withdrawals")]:
    for r in res_list:
        fc = r["Forecast"]; save_series(fname(target, r["Trend"], r["Seasonal"]), fc.index, fc.values, target)

print("Saved:", Path(OUT_BEST).resolve())
print("Saved:", Path(OUT_ALL).resolve())
print("Saved:", Path(OUT_METR).resolve())
