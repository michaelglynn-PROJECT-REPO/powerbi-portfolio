---
title: Zebra BI to Native Power BI Migration
description: Replacing third-party Zebra BI financial reporting visuals with maintainable native Power BI components, dynamic DAX and an optimised matrix design
---

[← Back to Portfolio Homepage](https://michaelglynn-project-repo.github.io/powerbi-portfolio/)

---

# Zebra BI to Native Power BI Migration

## Project Overview

This project involved rebuilding a set of financial reports that relied on **Zebra BI** visuals using only native Power BI components.

The objective was to reduce reliance on third-party licensing while preserving the existing report functionality, financial presentation and user experience. The replacement also needed to be easier to maintain and perform effectively across detailed financial reporting structures.

---

## My Responsibilities

I was responsible for:

- Reviewing the existing Zebra BI reports and identifying the functionality that needed to be retained
- Recreating financial matrices, waterfall-style visuals and KPI displays using native Power BI
- Developing the supporting DAX measures and display logic
- Implementing dynamic row behaviour, conditional formatting, tooltips and drill-through
- Testing the replacement reports against the original outputs
- Identifying and resolving report-performance issues

---

## Business Challenge

The existing reports used Zebra BI visuals to present actual, planned and variance figures across services, areas and divisions.

Replacing these visuals was challenging because native Power BI visuals did not provide all the same behaviour automatically. The new solution needed to reproduce:

- Hierarchical financial reporting
- Actual and planned values
- Monetary and percentage variances
- Dynamic row layouts
- Conditional indicators
- Drill-through to transaction-level detail
- Consistent behaviour across different organisational levels

---

## Solution

I recreated the reporting experience using native Power BI matrices, charts and KPI visuals.

A supporting **LabelDimMap** structure was used to control the order, format and behaviour of financial rows. DAX measures dynamically returned the appropriate result based on the selected financial label and reporting context.

The completed solution included:

- Dynamic financial matrix layouts
- Actual, planned and variance calculations
- YTD and ITM reporting logic
- Monetary and percentage formatting
- Conditional formatting and directional indicators
- Custom report-page tooltips
- Drill-through to transaction-level details
- Service, area and division reporting views

---

## Tools and Techniques

- Power BI Desktop
- DAX
- Power Query
- Native matrix and chart visuals
- Dynamic measure selection
- Filter-context and scope management
- Conditional formatting
- Report-page tooltips
- Drill-through
- Performance Analyzer
- Semantic-model optimisation

---

## Performance Improvement

During development, a complex financial matrix initially took approximately **82 seconds** to load.

By reviewing the DAX logic, visual configuration and evaluation context, I reduced the loading time to approximately **8 seconds**.

**Result: approximately 90% faster visual loading.**

This significantly improved the report experience while retaining the required financial detail and functionality.

---

## Before and After

[View Original Zebra BI Report →](./visuals/Finance%20Reports%20for%20SM%20&%20AM%20(Before)%20REDACTED.pdf)

[View Native Power BI Replacement →](./visuals/Finance%20Reports%20for%20SM%20&%20AM%20(After)%20REDACTED.pdf)

### Key Areas Recreated

- Financial matrices
- Waterfall-style reporting
- KPI summaries
- Conditional variance indicators
- Service, area and divisional reporting
- Transaction-level drill-through

---

## Outcome

The completed report replaced the required Zebra BI functionality with native Power BI components.

The migration:

- Reduced reliance on third-party visuals
- Improved report maintainability
- Preserved the required financial reporting functionality
- Improved matrix performance
- Provided greater control over DAX, formatting and interaction behaviour

---

## Reflection

This project strengthened my understanding of DAX evaluation context, dynamic matrix design and Power BI performance optimisation.

The main challenge was not simply recreating the appearance of the Zebra BI reports, but reproducing their behaviour using maintainable native components. This required careful management of row-level logic, filter context, formatting and organisational hierarchies.

---

## Disclaimer

This portfolio version contains redacted or anonymised content. Names, email addresses, internal codes and financial figures have been removed or replaced where required.

The report structure, visual design and technical logic have been retained to demonstrate the Power BI solution without disclosing confidential organisational data.
```
