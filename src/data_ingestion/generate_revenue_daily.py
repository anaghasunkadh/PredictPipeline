# Import libraries (pandas, numpy, datetime)
import pandas as pd
import numpy as np
from datetime import datetime

# Generate date range from 2023-01-01 to today
date_daily = pd.date_range(start="2023-01-01",end="today")
active_customers = 100
revenue_data = []
# Loop through each date
for date in date_daily:
    new_customers = np.random.randint(5,20)
    churned_customers=np.random.randint(0,5)
    active_customers = active_customers +new_customers -churned_customers
    daily_revenue =active_customers*150/30
    MRR = active_customers*150
    revenue ={
        'date':date,
        'new_customers':new_customers,
        'churned_customers':churned_customers,
        'active_customers':active_customers,
        'daily_revenue':daily_revenue,
        'MRR':MRR


    }
    
    revenue_data.append(revenue)
df= pd.DataFrame(revenue_data)
df.to_csv("data/raw/revenue_daily.csv", index=False)
print(f"Generated {len(revenue_data)} revenue data and saved to CSV")

