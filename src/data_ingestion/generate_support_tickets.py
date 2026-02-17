from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
fake = Faker()
tickets =[]
for i in range(10000):
    ticket_id = np.random.randint(1,10000)
    user_id= np.random.randint(1,10000)
    created_date= fake.date_between(start_date='-20y',end_date='today')
    priority= np.random.choice(['Low','Medium','High','Critical'])
    category = np.random.choice(['Bug','Feature Request','Question','Account Issue'])
    status = np.random.choice(['Open','In Progress','Resolved','Closed'])
    if status in ['Resolved','Closed']:
        resolved_date = fake.date_between(start_date=created_date, end_date='today')
        resolution_time_hours = (resolved_date - created_date).total_seconds() / 3600
        
    else:
        resolved_date = None
        resolution_time_hours = None
    ticket = {
    'ticket_id':ticket_id,
    'user_id':user_id,
    'created_date':created_date,
    'resolved_date':resolved_date,
    'priority':priority,
    'category':category,
    'status':status,
    'resolution_time_hours':resolution_time_hours
    }
    tickets.append(ticket)
df= pd.DataFrame(tickets)
df.to_csv("data/raw/support_tickets.csv", index=False)
print(f"Generated {len(tickets)} support tickets and saved to CSV")







    
