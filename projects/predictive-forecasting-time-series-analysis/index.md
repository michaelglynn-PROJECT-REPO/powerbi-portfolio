---
title: Predictive Forecasting of Enrolments & Withdrawals
description: Python + Power BI time-series forecasting using Holt-Winters, ADF testing, RMSE evaluation, and Databridge SQL data engineering.
---

[← Back to Portfolio Homepage](https://michaelglynn-project-repo.github.io/powerbi-portfolio/)

---

## Goal
Develop an end-to-end forecasting pipeline that extracts monthly qualification activity from Databridge SQL, models trends using Python (Holt-Winters ETS), and visualises future enrolments and withdrawals in Power BI to support planning and decision-making.

---

## Key Features
- Python forecasting pipeline using Holt-Winters Exponential Smoothing  
- 12-month rolling RMSE cross-validation  
- ADF testing for trend and stationarity analysis  
- Dynamic forecasting horizon (aligned to academic-year boundaries)  
- Power BI reporting combining actuals with forecasted values  
- Automated SQL-based month spine and metric aggregation  

---

## Tools & Techniques
- **Python:** pandas, statsmodels, scikit-learn  
- **SQL:** Databridge MIS  
- **Power BI:** DAX, model design, forecasting visuals  
- Holt–Winters additive & multiplicative models  
- ADF stationarity testing  
- RMSE / NRMSE scoring and fallback seasonal naïve models  

---

## Visuals
[View Forecasting Report (Redacted PDF)](./visuals/Proj3%20PBI%20REDACTED.pdf)

Highlights include:  
- Forecast overlays for enrolments and withdrawals  
- Academic-year slicing  
- Trend and seasonality decomposition  
- Scenario-ready export layout for Power BI  

---

## Commentary
This project combined SQL extraction, Python modelling, and Power BI dashboarding into a unified workflow.  
I built a custom forecasting engine that evaluates multiple trend/seasonal model combinations, applies cross-validated RMSE scoring, performs ADF diagnostics, and exports the most robust forecast to Power BI.

The project strengthened my understanding of time-series modelling, forecasting evaluation, and automated data engineering.

---

## Files

### Python Source
- [analyse.py](./analyse.py)  
- [import_transform.py](./import_transform.py)

### Power BI Export (Redacted)
- [Forecasting Report PDF](./visuals/Proj3%20PBI%20REDACTED.pdf)

---

## Disclaimer
All qualification names, student counts, business units, and internal organisational details have been anonymised or replaced with placeholder values.  
The forecasting logic, modelling approach, and Power BI layout are preserved for demonstration purposes only.  
No real learner or organisational data is shared in this version.

