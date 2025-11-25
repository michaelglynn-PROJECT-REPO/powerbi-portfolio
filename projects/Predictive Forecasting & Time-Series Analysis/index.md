---
title: Predictive Forecasting of Enrolments & Withdrawals
description: Python + Power BI time-series forecasting using Holt-Winters, ADF testing, RMSE evaluation, and Databridge SQL data engineering.
---

[← Back to Portfolio Homepage](https://michaelglynn-project-repo.github.io/powerbi-portfolio/)

---

## Project Goal:
Build an end-to-end predictive forecasting pipeline that extracts monthly qualification activity from Databridge SQL, models trends using Python (Holt-Winters ETS), and visualises future enrolments and withdrawals inside Power BI.

---

## Key Features:
Python forecasting pipeline (Holt-Winters ETS)

12-month rolling RMSE cross-validation

ADF testing for trend/stationarity checks

Dynamic forecasting horizon (to next academic year)

Power BI report overlaying actuals vs forecast

Automated month spine + metric aggregation

---

## Tools & Techniques
Python (pandas, statsmodels, scikit-learn)

SQL (Databridge MIS)

Power BI Desktop

Holt-Winters Exponential Smoothing (additive & multiplicative)

ADF stationarity testing

RMSE, NRMSE, and fallback seasonal naïve models

---

## Visuals
[View Project 3 Power BI PDF (Redacted)](./visuals/Proj3%20PBI%20REDACTED.pdf)

Highlights: Forecast overlays, academic-year slicing, enrolment/withdrawal trend decomposition.

---

## Commentary
This project combined SQL extraction, Python modelling, and Power BI dashboarding into one workflow.  
I developed a custom forecasting engine that evaluates multiple trend/seasonal combinations, applies cross-validated RMSE scoring, performs ADF diagnostics, and exports the best model to Power BI for reporting.

It strengthened my understanding of time-series modelling and automated data engineering.

---

## Files
Python source:  
- [`analyse.py`](../path/analyse.py) :contentReference[oaicite:0]{index=0}  
- [`import_transform.py`](../path/import_transform.py) :contentReference[oaicite:1]{index=1}

Power BI Export (Redacted):  
- [`Proj3 PBI.pdf`](./visuals/Proj3%20PBI%20REDACTED.pdf) :contentReference[oaicite:2]{index=2}

---

## **Disclaimer**:  
All qualification names, student counts, business units, and internal organisational details have been anonymised or replaced with placeholder values.  
The forecasting logic, modelling approach, and Power BI layout are preserved for demonstration only.  
No real learner or organisational data is shared in this version.
