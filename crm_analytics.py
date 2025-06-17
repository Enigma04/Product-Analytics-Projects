import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('crm.csv')
print(df.columns.tolist())
df.head()

for col in ['signup_date', 'event_date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Drop rows without valid dates
df = df.dropna(subset=['user_id', 'signup_date', 'event_date'])
df.info()

# Derive the cohort for each user
df['cohort_month'] = df.groupby('user_id')['signup_date'].transform('min').dt.to_period('M')

# Derive the activity month
df['activity_month'] = df['event_date'].dt.to_period('M')

# Count unique users per cohort and activity month
cohort_data = df.groupby(['cohort_month', 'activity_month'])['user_id'].nunique().reset_index()

# Pivot into matrix format
cohort_pivot = cohort_data.pivot(
    index='cohort_month',
    columns='activity_month',
    values='user_id'
)

# Determine diff cohort sizes (first column)
cohort_sizes = cohort_pivot.iloc[:, 0]

# Compute retention rates
retention = cohort_pivot.divide(cohort_sizes, axis=0).round(3) * 100

plt.figure(figsize=(10, 6))
plt.imshow(retention, aspect='auto', cmap='Blues', interpolation='nearest')
plt.colorbar(label='Retention Rate (%)')
plt.xticks(
    range(retention.shape[1]),
    [f"{i}\u207a" for i in range(retention.shape[1])],  # Month offsets
    rotation=45
)
plt.yticks(range(retention.shape[0]), retention.index.astype(str))
plt.title("Monthly Cohort Retention")
plt.xlabel("Months Since Signup")
plt.ylabel("Cohort Month")
plt.tight_layout()
plt.show()
