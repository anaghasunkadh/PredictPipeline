import pandas as pd
import great_expectations as gx
import os
os.makedirs("data/quarantine",exist_ok=True)
context = gx.get_context()
def handle_failures(df, results,name):
    if not results["success"]:
            for expectation in results["results"]:
                if not expectation["success"]:
                    bad_columns = expectation["expectation_config"]["kwargs"]["column"]
                    check_type = expectation["expectation_config"]["expectation_type"]
                    if check_type == "expect_column_values_to_not_be_null":
                        bad_rows = df[df[bad_columns].isnull()]
                    elif check_type == "expect_column_values_to_be_unique":
                        bad_rows = df[df[bad_columns].duplicated()]
                    elif check_type == "expect_column_values_to_be_in_set":
                        bad_rows = df[~df[bad_columns].isin(expectation["expectation_config"]["kwargs"]["value_set"])]
                    elif check_type == "expect_column_values_to_be_between":
                        bad_rows = df[(df[bad_columns] < expectation["expectation_config"]["kwargs"]["min_value"]) | (df[bad_columns] > expectation["expectation_config"]["kwargs"]["max_value"])]
                    bad_rows.to_csv(f"data/quarantine/{bad_columns}_{name}csv", index=False)
def validate_orders():
    orders= pd.read_csv("data/raw/instacart/orders.csv")
    validator = gx.from_pandas(orders)
    validator.expect_column_values_to_not_be_null("order_id")
    validator.expect_column_values_to_be_unique("order_id")
    validator.expect_column_values_to_be_in_set("eval_set",["prior","train","test"])
    validator.expect_column_values_to_be_between("order_dow", 0, 6)
    validator.expect_column_values_to_be_between("order_hour_of_day", 0, 23)
    results = validator.validate()
    print(results)
    handle_failures(orders, results,"orders")
def validate_products():
    products= pd.read_csv("data/raw/instacart/products.csv")
    validator = gx.from_pandas(products)
    validator.expect_column_values_to_not_be_null("product_id")
    validator.expect_column_values_to_not_be_null("product_name")
    validator.expect_column_values_to_not_be_null("aisle_id")
    validator.expect_column_values_to_not_be_null("department_id")
    validator.expect_column_values_to_be_unique("product_id")
    results = validator.validate()
    print(results)
    handle_failures(products, results,"products")
def validate_rossman():
    rossmann =pd.read_csv("data/raw/rossmann/train.csv")
    validator = gx.from_pandas(rossmann)
    validator.expect_column_values_to_be_between("DayOfWeek",1, 7)
    validator.expect_column_values_to_be_between("Sales", 0, None)
    validator.expect_column_values_to_be_between("Customers", 0, None)
    validator.expect_column_values_to_be_in_set("Open", [0, 1])
    validator.expect_column_values_to_be_in_set("Promo", [0, 1])
    validator.expect_column_values_to_be_in_set("SchoolHoliday", [0, 1])
    validator.expect_column_values_to_be_in_set("StateHoliday",["a","b","c","0"])
    results = validator.validate()
    print(results)
    handle_failures(rossmann, results,"rossmann")
def validate_retailTransaction():
    retailTransaction = pd.read_csv("data/raw/online-retail-ii-uci/online_retail_II.csv")
    validator = gx.from_pandas(retailTransaction)
    validator.expect_column_values_to_not_be_null("Invoice")
    validator.expect_column_values_to_not_be_null("StockCode")
    validator.expect_column_values_to_be_between("Price", min_value=0, max_value=None)
    validator.expect_column_values_to_not_be_null("Country")
    results = validator.validate()
    print(results)
    handle_failures(retailTransaction, results, "retailTransaction")
if __name__ == "__main__":
    validate_orders()
    validate_products()
    validate_rossman()
    validate_retailTransaction()








