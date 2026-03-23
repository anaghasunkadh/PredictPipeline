from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
class RetailTransaction(BaseModel):
    Invoice:str
    StockCode:str
    Description:str
    Quantity:int
    InvoiceDate:date
    Price:float
    Customer:Optional[int]
    Country:str
class Orders(BaseModel):
    order_id:int
    user_id:int
    eval_set:str
    order_number:int
    order_dow:int
    order_hour_of_day:int
    days_since_prior_order:Optional[int]
class Rossmannsales(BaseModel):
    Store:int
    DayOfWeek:int
    Date:date
    Sales:int
    Customers:int
    Open:int
    Promo:int
    StateHoliday:str
    SchoolHoliday:int
class Products(BaseModel):
    product_id:int
    product_name:str
    aisle_id:int
    department_id:int