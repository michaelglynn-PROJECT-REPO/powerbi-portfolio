# ---Module Imports---
import pandas as pd
import pyodbc
from datetime import date
start = date(2018,8,1)

# ---Connect to SQL DB---
cn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server= -------------------------;"
    "Database= ---------------------;"
    "Uid= ------;"
    "Pwd= -----------;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# ---Select Statement---
sql = """
DECLARE @StartDate date = ?;
SELECT
  sq.Student_Qualification_ID   AS StudentQualificationID,
  sq.Student_ID                 AS StudentID,
  sq.Qualification_ID           AS QualificationID,
  sq.StartDate                  AS EnrolmentDate,
  sq.ExpectedEndDate            AS ExpectedEndDate,
  sq.EndDate                    AS ActualEndDate,
  st.Status_Name                AS StatusName,
  q.Qualification_Name          AS QualificationName
FROM dbo.tbl_Exams_Student_Qualification sq
LEFT JOIN dbo.tbl_Exams_Qualification q ON q.Qualification_ID = sq.Qualification_ID
LEFT JOIN dbo.tbl_Exams_Status       st ON st.Status_ID       = sq.Status_ID
WHERE sq.StartDate >= @StartDate;
"""
df = pd.read_sql(sql, cn, params=[start])

# ---Test Working---
# print("Rows returned:", len(df))
# print(df.head())

# ---Confirm Names---
print(df["StatusName"].dropna().unique())

# ---Status Names---
withdrawal_labels = {"Did Not Complete (Withdrawn from the learning aim)"}
completion_labels = {
    "Completed and Achieved the learning aims",
    "Completed NOT achieved the learning aim",
    "Learning activities Complete, result not yet known"
}

# ---Flag Set---
df["IsWithdrawal"] = df["StatusName"].isin(withdrawal_labels).astype(int)
df["IsCompletion"] = df["StatusName"].isin(completion_labels).astype(int)

# Month spine (Aug–Jul)
months = pd.date_range(start, df[["EnrolmentDate","ActualEndDate"]].max().max(), freq="MS")
spine = pd.DataFrame({"MonthStart": months})
spine["MonthEnd"] = spine["MonthStart"] + pd.offsets.MonthEnd(0)
spine["AcademicYear"] = spine["MonthStart"].apply(
    lambda d: f"{d.year}/{str(d.year+1)[2:]}" if d.month>=8 else f"{d.year-1}/{str(d.year)[2:]}"
)

# ---Aggregate by Month---
def month_agg(ms, me, ay):
    sel_enr = (df["EnrolmentDate"].between(ms, me))
    sel_end = df["ActualEndDate"].between(ms, me)

    enr  = df.loc[sel_enr].groupby("QualificationID").size()
    wd   = df.loc[sel_end & (df["IsWithdrawal"]==1)].groupby("QualificationID").size()
    comp = df.loc[sel_end & (df["IsCompletion"]==1)].groupby("QualificationID").size()
    act  = df.loc[(df["EnrolmentDate"]<=me) & (df["ActualEndDate"].isna() | (df["ActualEndDate"]>=ms))] \
             .groupby("QualificationID").size()

    out = pd.DataFrame({
        "Enrolments": enr, "Withdrawals": wd, "Completions": comp, "ActiveHeadcount": act
    }).fillna(0).astype(int).reset_index()
    out["MonthStart"]=ms; out["MonthEnd"]=me; out["AcademicYear"]=ay
    return out

monthly = pd.concat([month_agg(r.MonthStart, r.MonthEnd, r.AcademicYear) for r in spine.itertuples()], ignore_index=True)

# ---Join Labels---
labels = df[["QualificationID","QualificationName"]].drop_duplicates()
monthly = monthly.merge(labels, on="QualificationID", how="left")

# ---Save Output---
monthly.to_csv("project3_monthly_metrics.csv", index=False)
print("Rows:", len(monthly)); print(monthly.head())
