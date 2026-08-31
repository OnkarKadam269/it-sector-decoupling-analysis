# Revenue-Headcount Decoupling in Indian IT: A Currency-Adjusted Analysis

**Is Indian IT's revenue growth genuinely driven by productivity gains — or is it largely a currency illusion?**

A data-driven investigation into whether the "AI is boosting IT sector productivity" narrative holds up once nominal INR figures are adjusted for rupee depreciation, using quarterly financial disclosures from India's five largest listed IT services companies, cross-validated against official NASSCOM sector data.

---

## Table of Contents
- [Business Question](#business-question)
- [Key Findings](#key-findings)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Tech Stack](#tech-stack)
- [Dashboard](#dashboard)
- [Repository Structure](#repository-structure)
- [Limitations](#limitations)
- [Conclusion](#conclusion)

---

## Business Question

Between FY22 and FY25, Indian IT sector revenue has consistently outpaced headcount growth, sparking a popular narrative that AI adoption is driving a step-change in workforce productivity. This project tests that claim rigorously by asking three questions:

1. Is revenue genuinely decoupling from headcount growth at the sector level?
2. How much of that decoupling survives after removing the effect of rupee depreciation against the US dollar?
3. Is the pattern consistent across companies, or driven by a few outliers?

---

## Key Findings

### 1. The headline number is real — but overstated

| Metric | Nominal (INR) | Real (USD, currency-adjusted) |
|---|---|---|
| Revenue growth (16 quarters) | **40.8%** | **20.6%** |
| Headcount growth (16 quarters) | 19.2% | 19.2% |
| Revenue-to-headcount growth multiplier | **2.1x** | **1.07x** |

Nearly **half of the apparent revenue growth (20.2 percentage points) is explained by rupee depreciation**, not underlying business performance. Once currency effects are removed, revenue barely outpaced headcount growth at the sector level.

### 2. Real productivity per employee shows a V-shape, not steady growth

Currency-adjusted revenue-per-employee **declined ~7%** from mid-2021 through late 2022 (post-pandemic over-hiring diluted output per head), then recovered gradually. Over the full four-year window, net real productivity gain is only **~1.2%** — essentially flat, not the dramatic gain the nominal INR figures suggest.

### 3. The trend is inconsistent across companies

| Company | Real Productivity Change (4-yr, USD) |
|---|---|
| TCS | +2.97% |
| Infosys | +0.89% |
| HCLTech | +0.78% |
| Wipro | -5.32% |
| Tech Mahindra | -7.14% |

Only 3 of 5 companies show any real productivity gain, and the gains are marginal. Two companies show outright declines.

### 4. No meaningful link between hiring cuts and productivity gains

Correlation between headcount change and real productivity change across the five companies: **-0.27** — a weak relationship. The data does not support a clean "companies that cut jobs got more productive" story.

### 5. The 5-company sample tracks the official sector benchmark

| Fiscal Year | Sector Revenue Growth (NASSCOM) | Sector Employment Growth (NASSCOM) |
|---|---|---|
| FY23 | 8.4% | 5.7% |
| FY24 | 3.8% | 1.1% |
| FY25 | 5.1% | 2.3% |

In every year, official sector-wide revenue growth outpaces employment growth — the same directional pattern seen in the 5-company sample — confirming the sample is representative rather than cherry-picked. Notably, the sample's own headcount **declined** over FY23-FY25 even while NASSCOM's national employment figure stayed positive, suggesting employment growth in the broader sector is being driven by smaller players and Global Capability Centres (GCCs) rather than the large listed IT majors.

---

## Data Sources

- **Company financials:** Quarterly revenue (INR Cr and USD Mn) and total headcount for TCS, Infosys, Wipro, HCLTech, and Tech Mahindra, sourced from official investor relations disclosures (earnings presentations, fact sheets, press releases), covering Q1 FY22 (quarter ended June 2021) through Q4 FY25 (quarter ended March 2025) — 16 consecutive quarters, 80 company-quarter observations.
- **Sector benchmark:** NASSCOM Strategic Review annual reports (FY23-FY26), providing official sector-wide revenue and employment growth rates for cross-validation.

---

## Methodology

1. **Data collection** — Quarterly financials gathered from official investor relations sources for all 5 companies, plus annual sector-wide figures from NASSCOM.
2. **Data cleaning & validation** — Type casting, duplicate checks, and sanity checks on revenue/headcount values (Python, pandas).
3. **Feature engineering** — Revenue-per-employee calculated at company and sector level; quarter-over-quarter growth rates computed per company.
4. **Indexed growth analysis** — Revenue and headcount rebased to 100 at Q1 FY22 to enable direct visual and numerical comparison of growth trajectories ("the decoupling gap").
5. **Currency adjustment** — The same indexing methodology applied to USD-denominated revenue to isolate real business growth from currency-driven nominal growth.
6. **Cross-validation** — Company-sample fiscal-year aggregates compared against NASSCOM's official annual sector growth rates to test representativeness.
7. **Company-level breakdown & correlation testing** — Individual company productivity changes calculated and tested for correlation with headcount changes.
8. **SQL analysis layer** — Cleaned data loaded into a SQLite database; ranking and aggregation queries used to validate and structure company-level and sector-level views.
9. **Dashboard development** — A 2-page Power BI dashboard built to present the narrative: (1) the trend and its currency-adjusted reality check, and (2) the company-level breakdown and final validated conclusion.

---

## Tech Stack

- **Python** (pandas, NumPy, Matplotlib) — data cleaning, feature engineering, statistical analysis, visualization
- **SQL** (SQLite) — data querying, aggregation, ranking
- **Power BI** — interactive dashboard with DAX measures (including a manually-built Pearson correlation formula), synced cross-page slicers, and conditional formatting
- **DAX** — custom measures for growth rates, currency contribution, and productivity-headcount correlation

---

## Dashboard

A 2-page interactive Power BI dashboard:

- **Page 1 — Trend & Reality Check:** KPI cards for nominal vs real growth, indexed revenue-vs-headcount trend line, and the currency-adjusted revenue-per-employee comparison.
- **Page 2 — Company Breakdown & Verdict:** Company-level productivity bar chart (color-coded by gain/decline), NASSCOM validation table, correlation KPI, and final narrative conclusion.

*(Add dashboard screenshots here before publishing — e.g. `/images/dashboard_page1.png`, `/images/dashboard_page2.png`)*

---

## Repository Structure

```
├── data/
│   ├── company_quarterly_data.xlsx        (raw collected data)
│   ├── nasscom_sector_data.xlsx           (raw collected data)
│   ├── company_level_clean.xlsx           (cleaned, Python output)
│   ├── sector_quarterly_summary.xlsx      (cleaned, Python output)
│   ├── sector_quarterly_usd.xlsx          (cleaned, Python output)
│   ├── company_productivity_summary.xlsx  (cleaned, Python output)
│   └── nasscom_comparison.xlsx            (cleaned, Python output)
├── notebooks/
│   ├── build_final_csvs.py                (data collection/export script)
│   └── analysis.ipynb                     (full Python analysis notebook)
├── sql/
│   └── it_sector_analysis.db              (SQLite database)
├── dashboard/
│   └── IT_Sector_Decoupling.pbix          (Power BI dashboard, 2 pages)
├── images/
│   ├── revenue_headcount_decoupling.png
│   ├── currency_adjusted_productivity.png
│   ├── dashboard_page1.png                (add: screenshot your Power BI Page 1)
│   └── dashboard_page2.png                (add: screenshot your Power BI Page 2)
└── README.md
```

---

## Limitations

- The 5-company sample represents large-cap listed IT services majors; results may not generalize to smaller IT firms, startups, or Global Capability Centres (GCCs), which appear to be a growing share of sector employment.
- Revenue-per-employee is a blunt productivity proxy; it does not account for changes in service mix, deal pricing, or subcontracted/offshore labor not reflected in reported headcount.
- Correlation analysis on company-level productivity vs. headcount change uses only 5 data points and should be treated as directional, not statistically robust.
- This analysis establishes correlation between time period and productivity metrics, not causation — it does not isolate AI adoption specifically from other contributing factors (pricing power, deal mix shifts, macroeconomic demand cycles).

---

## Conclusion

Nominal revenue grew 2.1x faster than headcount over the study period — but nearly half of this apparent decoupling is explained by rupee depreciation rather than genuine productivity improvement. In real, currency-adjusted terms, sector-wide productivity gains are small (1-3%) among top performers and negative at others, with no statistically meaningful link between workforce reductions and productivity gains. This suggests that AI-driven efficiency in India's largest IT services companies remains an early-stage, uneven trend rather than a broad, already-realized transformation — a more precise and defensible conclusion than the popular "AI is driving an IT productivity boom" narrative.

---

*This project was built independently as a self-directed data analysis exercise using publicly disclosed company financials and NASSCOM sector reports.*
