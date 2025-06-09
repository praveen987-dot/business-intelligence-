import pandas as pd
import os
from datetime import datetime

def clean_ethereum_data(raw_filepath, save_path='etl_project/data'):
    df = pd.read_csv(raw_filepath)

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.drop_duplicates(subset='timestamp', inplace=True)
    df.dropna(inplace=True)
    df = df[(df['price'] > 0) & (df['volume'] >= 0)]
    df.sort_values('timestamp', inplace=True)

    os.makedirs(save_path, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    clean_filepath = os.path.join(save_path, f'ethereum_cleaned_data.csv')
    df.to_csv(clean_filepath, index=False)
    print(f"Cleaned data saved to \n{clean_filepath}\n\n")
    return clean_filepath

if __name__ == "__main__":
    path_to_raw_csv = 'etl_project/data/ethereum_raw_data.csv'
    clean_ethereum_data(path_to_raw_csv)
