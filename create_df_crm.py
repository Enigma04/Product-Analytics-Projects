import pandas as pd
import numpy as np

# Simulated 100 users signing up over 3 months
np.random.seed(0)
users = pd.DataFrame({
    'user_id': np.arange(1, 101),
    'signup_date': pd.to_datetime(np.random.choice(pd.date_range('2025-01-01', '2025-04-19'), 100))
})

# Simulated each user doing 1-6 events after signup
events = []
for _, row in users.iterrows():
    n_events = np.random.randint(1, 7)
    for i in range(n_events):
        events.append({
            'user_id': row['user_id'],
            'signup_date': row['signup_date'],
            'event_date': row['signup_date'] + pd.Timedelta(days=np.random.randint(0, 90))
        })
df = pd.DataFrame(events)
print(df)
df.to_csv('crm.csv')
