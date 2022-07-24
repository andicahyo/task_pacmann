import pandas as pd

from helper.data_check_preparation import read_data
from helper.feature_engineering import feature_engineering

def auto_check():
    # pembacaan data
    df = read_data(PATH, encoding='cp1252')
    
    # feature enginering
    df_transformed = feature_engineering(df)
    print("Start Saving Result Feature Engineering!")
    df_transformed.to_csv("./data/autos_clean.csv")
    
    
if __name__ == "__main__":
    print("START RUNNING PIPELINE!")
    auto_check()
    print("FINISH RUNNING PIPELINE!")