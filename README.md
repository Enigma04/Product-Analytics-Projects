# Product Analytics Portfolio: Cohort Retention & Funnel Conversion

This repository showcases essential product analytics skills through two core analyses:

1) Monthly Cohort Retention Analysis - Measuring user engagement over time

2) Funnel Conversion Analysis - Tracking user progression through key stages

# Key Analyses
1. Monthly Cohort Retention Analysis
Objective: Measure how user engagement evolves over time for different signup cohorts

Technical Approach:
```
df['cohort_month'] = df.groupby('user_id')['signup_date'].transform('min').dt.to_period('M')
df['activity_month'] = df['event_date'].dt.to_period('M')
cohort_data = df.groupby(['cohort_month', 'activity_month'])['user_id'].nunique()
retention = cohort_pivot.divide(cohort_sizes, axis=0) * 100 
```
![monthly cohort retention](https://github.com/user-attachments/assets/ba0f06b9-a2da-47c2-b17d-cdedd0275ceb)

Key Insights from Results:

1. January 2025 cohort shows strongest retention (over 80% in Month 3)

2. Gradual retention decay observed across all cohorts

3. April 2025 cohort shows highest initial drop-off

4. Significant retention cliff between Months 1-2

Business Impact:

1. Identifies high-value acquisition periods

2. Quantifies long-term product stickiness

3. Highlights opportunities for retention improvement

4. Measures effectiveness of engagement initiatives


2. Funnel Conversion Analysis
Objective: Analyze user progression through critical conversion stages

Technical Approach:
```
counts = {
    'Started': started_mask.sum(),
    'Added to cart': added_mask.sum(),
    'Purchased': bought_mask.sum()
}
funnel['Conv. from Prev (%)'] = funnel['Count'].pct_change().fillna(1) * 100
```
![Conversion funnel](https://github.com/user-attachments/assets/c2dc15e2-9fee-48ec-ac51-42fddeee3e2b)

Key Insights from Results:

1. Major drop-off between cart addition (1750) and purchase (500)

2. Only 28.6% of users who add to cart complete purchase

3. Initial conversion from start to cart is strong (87.5%)

4. Significant revenue opportunity in cart abandonment recovery

Business Impact:

1. Pinpoints biggest conversion bottleneck (cart to purchase)

2. Quantifies potential revenue lift from improvements

3. Prioritizes UX optimization areas

4. Benchmarks campaign effectiveness

# Technical Skills Demonstrated
📈 Analytical Techniques

Cohort Analysis: Time-based user segmentation

Funnel Analysis: Conversion stage tracking

Retention Metrics: Longitudinal engagement patterns

Drop-off Quantification: Bottleneck identification

💻 Technical Execution

Python Stack: pandas, matplotlib, numpy

Data Wrangling: Datetime operations, missing value handling

Statistical Analysis: Rate calculations, percentage changes

Data Visualization: Heatmaps, funnel charts

🔍 Business Acumen

Translating data insights into business opportunities

Prioritizing high-impact improvement areas

Quantifying potential revenue impact

Measuring product stickiness over time

