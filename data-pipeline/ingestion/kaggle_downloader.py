import os
import sys
from dotenv import load_dotenv
load_dotenv()
import kaggle
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
if KAGGLE_USERNAME is None or KAGGLE_KEY is None:
    print("You need environment variables")
    sys.exit(1)
kaggle.api.authenticate()
def download_dataset(dataset_id, destination_path):
    try:
        if not os.path.exists(destination_path):
            print(f"downloading{dataset_id}")
            kaggle.api.dataset_download_files(dataset_id,destination_path,unzip=True)
        else:
            print(f"skipping{dataset_id}")
    except Exception as e:
        print(e)
        sys.exit(1)
download_dataset("mashlyn/online-retail-ii-uci","data/raw/online-retail-ii-uci/")
download_dataset("psparks/instacart-market-basket-analysis", "data/raw/instacart/")
download_dataset("pratyushakar/rossmann-store-sales", "data/raw/rossmann/")