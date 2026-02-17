from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime
fake = Faker()
events=[]
for i in range(100000):
    event_id =np.random.randint(1,100000)
    user_id =np.random.randint(1,10000)
    event_type=np.random.choice(['login','create_task','complete_task','update_task','create_board','invite_member',
    'add_comment','upload_file'])
    event_timestamp =fake.date_between('-3y','today')
    session_duration_minutes = np.random.randint(1,200)
    device_type = np.random.choice(['Desktop','Mobile','Tablet'])
    event = {
      
      'event_id':event_id,
      'user_id' :user_id,
      'event_type':event_type,
      'event_timestamp':event_timestamp,
      'session_duration_minutes':session_duration_minutes,
      'device_type' :device_type
    }
    events.append(event)
pd.DataFrame(events).to_csv("data/raw/usage_events.csv", index=False)
print(f"Generated {len(events)} usage events and saved to CSV")
    



    


