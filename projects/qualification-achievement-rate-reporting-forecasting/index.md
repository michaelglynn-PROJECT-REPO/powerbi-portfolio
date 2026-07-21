---
title: Qualification Achievement Rate Reporting & Forecasting
description: An end-to-end Power BI solution aligning internal qualification data with DfE reporting rules, national benchmarks and forward forecasts.
---

[← Back to Portfolio Homepage](https://michaelglynn-project-repo.github.io/powerbi-portfolio/)

---

# Qualification Achievement Rate Reporting & Forecasting

## Project Overview

This project involved developing a Power BI solution for analysing **Qualification Achievement Rates (QAR)** across academic years.

The solution transformed learner qualification records from an internal management information system into reporting measures aligned with Department for Education methodology.

It also incorporated national benchmark data and forward forecasts to provide both historical and future-focused insight.

The report was designed to support performance monitoring, identify areas requiring further investigation and provide a clearer understanding of achievement, retention and pass rates.

---

## Business Challenge

Qualification performance could not be measured accurately using simple counts of completed or withdrawn learning aims.

The reporting process needed to account for:

- Different qualification outcome statuses
- Continuing learners
- Planned and actual end dates
- Academic reporting-year allocation
- Excluded learning aims
- Withdrawal-reason rules
- Restarted qualifications
- National benchmark comparisons
- Differences between achievement, retention and pass rates

The challenge was to translate complex reporting methodology into a transparent, repeatable and maintainable Power BI solution.

---

## My Responsibilities

I was responsible for the complete reporting workflow, including:

- Identifying the relevant qualification, learner and status data
- Interpreting the required QAR reporting methodology
- Transforming source data into reporting-ready structures
- Creating calculated columns for reporting-year and outcome classification
- Implementing exclusion and restart rules
- Developing DAX measures for achievement, retention and pass rates
- Integrating national benchmark data
- Creating analytical report pages and drill-down views
- Developing forecasts for future qualification performance
- Testing and reconciling report outputs

---

## Data Sources

The solution combined:

- Internal learner qualification data
- Qualification status and outcome information
- Learner demographic information
- Qualification and subject-area classifications
- National achievement-rate benchmark data
- Forecast outputs generated from historical academic-year results

All portfolio visuals have been redacted or anonymised to protect learner and organisational information.

---

## Reporting Methodology

Each qualification record was classified according to its status and reporting outcome.

The model identified:

- **Achievers:** learners who completed and achieved their qualification
- **Completers:** learners who completed their qualification, regardless of achievement
- **Leavers:** learners included in the achievement-rate denominator
- **Continuing learners:** qualifications that remained in progress
- **Withdrawals:** learners who left before completing their qualification
- **Excluded records:** qualifications removed under the applied reporting methodology

Additional logic was used to determine the correct reporting year using qualification start dates, planned end dates and actual end dates.

The solution also accounted for restarted qualifications within the permitted restart period, preventing eligible restarted aims from being incorrectly counted as withdrawals.

---

## Core Measures

The main performance measures were:

**Qualification Achievement Rate**

`QAR % = Achievers ÷ Leavers`

**Retention Rate**

`Retention % = Completers ÷ Leavers`

**Pass Rate**

`Pass % = Achievers ÷ Completers`

These measures responded dynamically to academic year, learner characteristics, qualification type and subject-area filters.

---

## Data Model

The Power BI model combined qualification-level fact data with supporting dimensions for:

- Academic year
- Qualification
- Learner demographics
- Subject sector area
- Qualification status
- National benchmarks
- Forecast results

Calculated columns were used to determine:

- Achievement status
- Completion status
- Continuing status
- Actual end year
- Planned end year
- Hybrid reporting year
- Exclusion status

The model allowed the same core measures to be analysed consistently across all report pages.

---

## Reporting-Year Logic

A hybrid reporting-year method was used to assign qualification records to the correct academic year.

The logic considered:

- Qualification start date
- Planned end date
- Actual end date
- Completion status
- Withdrawal status
- Whether the qualification was still in progress

This ensured that qualifications were counted in the reporting period required by the applied methodology rather than simply being grouped by their start date.

---

## Exclusion Logic

Certain qualification records were excluded from the headline QAR calculations.

The exclusion logic included:

- Specified withdrawal reasons
- Eligible restarted qualifications
- Records that did not meet the reporting methodology
- Qualifications outside the selected reporting scope

A dedicated exclusions page was included so that excluded records could be reviewed and validated.

This made the calculation process more transparent and helped support reconciliation.

---

## National Benchmarking

National achievement-rate data was included to compare internal performance against published benchmarks.

The report supported comparisons by:

- Academic year
- Provider type
- Subject sector area
- Achievement rate
- Retention rate
- Pass rate

This provided additional context and helped identify areas where internal performance was above or below comparable national results.

---

## Forecasting Approach

Historical annual performance was used to forecast future:

- Achievers
- Completers
- Leavers
- Qualification achievement rate
- Retention rate
- Pass rate

The forecasting process used Holt-Winters exponential smoothing models to identify historical patterns and estimate performance for the next academic year.

Forecast accuracy was evaluated using:

- **RMSE:** Root Mean Squared Error
- **NRMSE:** Normalised Root Mean Squared Error

The forecast outputs were loaded into Power BI and presented alongside historical results.

Forecasts were treated as planning indicators rather than guaranteed future outcomes.

---

## Report Pages

### Summary

The summary page presented:

- Qualification achievement rate
- Retention rate
- Pass rate
- Achiever, completer and leaver totals
- National benchmark comparisons
- Academic-year performance trends

### Exclusions

The exclusions page provided visibility of records excluded from the headline calculations.

This allowed users to review the records, reasons and rules affecting the final results.

### Demographics

The demographics page allowed qualification performance to be analysed across learner groups.

This included comparisons by characteristics such as age, gender and other available demographic fields.

### Subject Sector Area

Performance could be reviewed by subject sector area to identify stronger and weaker curriculum areas.

### Qualification Aims

The qualification aims page provided detailed qualification-level information, allowing users to investigate the records contributing to the overall results.

### Forecast

The forecast page compared historical performance with projected future results and included model-accuracy information.

---

## Tools and Techniques

- Power BI Desktop
- DAX
- Power Query
- SQL
- Python
- Data modelling
- Calculated columns
- Dynamic measures
- Filter-context management
- National benchmark integration
- Holt-Winters exponential smoothing
- RMSE and NRMSE evaluation
- Data validation and reconciliation

---

## Key Technical Features

- Dynamic academic-year selection
- Hybrid reporting-year classification
- Achievement, completion and leaver flags
- Withdrawal and restart exclusions
- National benchmark comparisons
- Demographic analysis
- Subject-area analysis
- Qualification-level drill-down
- Forecasting of future performance
- Model-accuracy reporting
- Transparent exclusion review

---

## Project Outcome

The completed solution created a consistent and transparent approach to qualification achievement reporting.

It provided:

- A repeatable QAR calculation process
- Clear separation of achievement, retention and pass rates
- Visibility of exclusions and reporting logic
- National benchmark comparisons
- Analysis across demographics, qualifications and subject areas
- Forward forecasts to support planning
- A single Power BI report for both summary and detailed investigation

The project demonstrated how complex external reporting methodology could be translated into a practical business intelligence solution.

---

## Visuals

[View QAR Reporting and Forecasting Report – Redacted PDF →](./visuals/qar-reporting-forecasting-redacted.pdf)

The report includes:

- QAR summary reporting
- Achievement, retention and pass-rate measures
- National benchmark comparisons
- Exclusion analysis
- Demographic analysis
- Subject-area analysis
- Qualification-level detail
- Historical and forecast performance

---

## Limitations and Future Improvements

Potential future improvements include:

- Automating the national benchmark data refresh
- Adding forecast confidence intervals
- Comparing additional forecasting approaches
- Introducing automated data-quality alerts
- Scheduling the complete source-to-report refresh process
- Adding further benchmark breakdowns
- Creating a dedicated reconciliation page for reporting-rule validation

---

## Reflection

This project strengthened my ability to translate complex reporting requirements into a structured Power BI solution.

The most challenging part was ensuring that reporting-year allocation, qualification outcomes, exclusions and restart rules worked together correctly.

Small changes to these rules could significantly affect the final achievement rates, making validation and transparency essential.

The project also developed my experience in combining business-rule interpretation, data modelling, DAX, external benchmarking and forecasting within a single reporting solution.

---

## Disclaimer

This portfolio version contains anonymised or redacted content.

Learner names, qualification details, internal identifiers, organisational information and sensitive figures have been removed or replaced where required.

The report structure, calculation methodology, data model and analytical approach have been retained to demonstrate the technical solution without disclosing confidential learner or organisational data.
