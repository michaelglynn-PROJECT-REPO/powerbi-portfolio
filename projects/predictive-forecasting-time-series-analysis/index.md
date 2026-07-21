---
title: Predictive Forecasting of Enrolments & Withdrawals
description: An end-to-end SQL, Python and Power BI forecasting solution using Holt-Winters exponential smoothing, model evaluation and automated data transformation.
---

[← Back to Portfolio Homepage](https://michaelglynn-project-repo.github.io/powerbi-portfolio/)

---

# Predictive Forecasting of Enrolments & Withdrawals

## Project Overview

This project involved developing an end-to-end forecasting solution for monthly qualification enrolments and withdrawals.

Historical learner activity was extracted from a Databridge SQL database, transformed and aggregated in Python, modelled using Holt-Winters exponential smoothing, and presented through an interactive Power BI report.

The purpose of the solution was to provide forward-looking insight that could support resource planning, learner monitoring and operational decision-making.

---

## Business Challenge

Historical reports showed what had already happened but did not provide an indication of likely future activity.

A forecasting solution was therefore required to:

- Identify recurring seasonal patterns
- Estimate future enrolment and withdrawal volumes
- Compare different forecasting configurations
- Measure model accuracy before producing future forecasts
- Present technical model outputs in a format suitable for business users
- Align reporting with academic-year periods

---

## My Responsibilities

I was responsible for the complete analytical workflow, including:

- Identifying the required learner and qualification data
- Writing the SQL extraction process
- Transforming and validating the source data in Python
- Creating monthly enrolment, withdrawal and completion metrics
- Building and comparing forecasting models
- Evaluating model accuracy using RMSE and NRMSE
- Exporting forecast outputs for Power BI
- Designing the Power BI report and analytical visuals
- Interpreting the results and documenting limitations

---

## Solution Architecture

**Databridge SQL → Python transformation → Forecast model evaluation → CSV outputs → Power BI report**

The solution was divided into two main Python processes:

1. **Data extraction and transformation**
   - Extract qualification records from Databridge SQL
   - Classify completed and withdrawn learning aims
   - Create a continuous monthly date spine
   - Aggregate monthly enrolments, withdrawals, completions and active learners

2. **Forecast modelling and evaluation**
   - Prepare monthly time-series data
   - Evaluate multiple Holt-Winters model configurations
   - Compare model accuracy
   - Select the strongest model for each target
   - Produce future forecasts through the configured academic-year horizon
   - Export actuals, forecasts and evaluation metrics for Power BI

---

## Data Preparation

The SQL extraction returned qualification-level records including:

- Qualification identifiers
- Enrolment dates
- Expected and actual end dates
- Qualification status
- Qualification names

Python was then used to:

- Classify qualification outcomes as completions or withdrawals
- Generate a continuous monthly date spine
- Aggregate qualification activity by month
- Create academic-year labels
- Calculate active learner headcount
- Prepare consistent time-series inputs for modelling

This approach ensured that months with no recorded activity were still represented in the dataset.

---

## Forecasting Method

The project used **Holt-Winters exponential smoothing** to model trend and seasonal behaviour.

Four model configurations were evaluated for each forecast target:

- Additive trend with additive seasonality
- Additive trend with multiplicative seasonality
- Multiplicative trend with additive seasonality
- Multiplicative trend with multiplicative seasonality

Separate models were evaluated for:

- Enrolments
- Withdrawals

Each target could therefore use the model configuration that performed best for its own historical pattern.

A seasonal naïve model was also included as a fallback where a Holt-Winters configuration could not be fitted successfully.

---

## Model Evaluation

The final 12 months of historical data were used as a holdout test period.

Each candidate model was fitted to the earlier data and used to predict the holdout period. Forecast performance was then assessed using:

- **RMSE:** Root Mean Squared Error
- **NRMSE by mean:** Error relative to the average observed value
- **NRMSE by range:** Error relative to the observed data range

The model with the lowest valid RMSE was selected separately for enrolments and withdrawals.

The project also calculated the **Augmented Dickey-Fuller test** as a diagnostic indicator of whether the historical series showed evidence of stationarity.

---

## Forecasting Features

- Holt-Winters exponential smoothing
- Additive and multiplicative model comparison
- Separate model selection for enrolments and withdrawals
- 12-month holdout evaluation
- RMSE and NRMSE accuracy measures
- Augmented Dickey-Fuller diagnostic testing
- Seasonal naïve fallback forecasting
- Automatic scaling and positive-value adjustment for multiplicative models
- Dynamic forecast horizon aligned with academic-year reporting
- Automated export of actuals, forecasts and model metrics

---

## Power BI Reporting

The Python outputs were loaded into Power BI to provide an accessible view of the forecast results.

The report included:

- Historical enrolment and withdrawal trends
- Actual versus forecast comparisons
- Forecast values by month
- Academic-year filtering
- Model accuracy metrics
- Trend and seasonal decomposition
- Next-period forecast indicators
- Comparison of alternative model configurations
- Commentary explaining the results and limitations

This allowed the technical model outputs to be presented in a format suitable for non-technical stakeholders.

---

## Project Outcome

The completed solution created a repeatable forecasting workflow combining SQL, Python and Power BI.

It demonstrated how historical operational data could be transformed into forward-looking information while retaining a clear validation process.

The project also provided:

- A consistent monthly qualification dataset
- Automated comparison of forecasting approaches
- Separate forecasts for enrolments and withdrawals
- Transparent model-performance measures
- Power BI-ready output files
- A reusable structure that could be refreshed with newer data

---

## Visuals

[View Forecasting Report – Redacted PDF →](./visuals/project-3-power-bi-redacted.pdf)

The report includes:

- Enrolment forecasting
- Withdrawal forecasting
- Historical and forecast overlays
- Academic-year analysis
- Model performance metrics
- Trend and seasonality analysis

---

## Source Files

### Python

- [View analyse.py →](./analyse.py)
- [View import_transform.py →](./import_transform.py)

### Power BI Report

- [View Forecasting Report PDF →](./visuals/project-3-power-bi-redacted.pdf)

---

## Limitations and Future Improvements

The forecasting results should be interpreted as planning indicators rather than guaranteed future values.

Potential improvements include:

- Implementing rolling-origin cross-validation across multiple test periods
- Adding confidence or prediction intervals
- Comparing Holt-Winters against SARIMA and Prophet
- Adding automated checks for structural changes in the data
- Introducing stronger treatment of unusual events and outliers
- Preventing negative forecasts for count-based measures
- Scheduling the complete SQL-to-Power BI refresh process

---

## Reflection

This project strengthened my understanding of time-series forecasting, model evaluation and automated analytical pipelines.

The most valuable aspect was combining several stages of the data lifecycle into one solution: SQL extraction, Python transformation, statistical modelling and Power BI presentation.

It also reinforced the importance of evaluating forecasting models against unseen historical data rather than selecting a model based only on how well it fits the training period.

---

## Disclaimer

This portfolio version contains anonymised or redacted content.

Qualification names, learner counts, internal organisational details and other sensitive information have been removed or replaced where required.

The data structure, modelling process, forecasting logic and Power BI report design have been retained to demonstrate the technical approach without disclosing confidential learner or organisational information.
