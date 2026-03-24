import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_validator import handle_failures
import pandas as pd
os.makedirs("data/quarantine", exist_ok=True)
def test_handle_failures():
    df = pd.DataFrame({
        "order_id": [1, 2, None],
        "name": ["a", "b", "c"]
    })
    
    results = {
        "success": False,
        "results": [
            {
                "success": False,
                "expectation_config": {
                    "expectation_type": "expect_column_values_to_not_be_null",
                    "kwargs": {
                        "column": "order_id"
                    }
                }
            }
        ]
    }
    
    name = "test"
    
    handle_failures(df, results, name)
    assert os.path.exists("data/quarantine/order_id_test.csv")