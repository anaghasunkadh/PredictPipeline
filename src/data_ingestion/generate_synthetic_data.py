from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
fake = Faker()
customers =[]
for i in range(10000):
    user_id = np.random.randint(1,10000)
    company_name= fake.company()
    company_size= np.random.choice(['small','medium','large'])
    plan_type= np.random.choice(['Basic','Pro','Enterprise'])
    subscription_status= np.random.choice(['Active','Churned'])
    signup_date = fake.date_between(start_date='-20y',end_date='today')
    if subscription_status == 'Churned':
        churn_date =  fake.date_between(start_date=signup_date,end_date='today')
    else:
        churn_date=None
    monthly_revenue=np.random.randint(10,5000)
    payment_method= np.random.choice(['Credit','Debit','Paypal'])
    #print(user_id,company_name,company_size,plan_type,subscription_status,signup_date,churn_date,monthly_revenue,payment_method)
    customer = {
    'user_id':user_id,
    'company_name':company_name,
    'company_size':company_size,
    'plan_type':plan_type,
    'subscription_status':subscription_status,
    'signup_date':signup_date,
    'churn_date':churn_date,
    'monthly_revenue':monthly_revenue,
    'payment_method':payment_method
    }
    customers.append(customer)
df= pd.DataFrame(customers)
df.to_csv("data/raw/customers.csv", index=False)
print(f"Generated {len(df)} customers and saved to CSV")
    







    
