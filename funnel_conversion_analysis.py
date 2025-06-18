#Funnel conversion Analysis

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Customer360Insights.csv')

print(df.columns.tolist())
df.head()

for col in ['SessionStart', 'CartAdditionTime', 'OrderConfirmationTime']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

df.info()

# Boolean masks
started_mask = df['SessionStart'].notna()
added_mask = df['CartAdditionTime'].notna()
bought_mask = df['OrderConfirmationTime'].notna()

# Count unique sessions or users at each stage
counts = {
    'Started': started_mask.sum(),
    'Added to cart': added_mask.sum(),
    'Purchased': bought_mask.sum(),
}

# Conversion to DataFrame

funnel = pd.DataFrame({
    'Stage': list(counts.keys()),
    'Count': list(counts.values())
})

# Compute conversion rate from previous stage
funnel['Conv. from Prev (%)'] = funnel['Count'].pct_change().fillna(1) * 100
funnel.loc[0, 'Conv. from Prev (%)'] = 100.0

plt.figure(figsize=(6, 4))
plt.bar(funnel['Stage'], funnel['Count'])
plt.title("Conversion Funnel")
plt.ylabel('Count')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()