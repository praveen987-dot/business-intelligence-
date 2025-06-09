import requests
import pandas as pd
from datetime import datetime
import os

def fetch_ethereum_data(vs_currency='usd', days='365', interval='daily'):
    url = 'https://api.coingecko.com/api/v3/coins/ethereum/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days,
        'interval': interval
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def process_and_save(data, save_path='etl_project/data'):
    os.makedirs(save_path, exist_ok=True)

    df_prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df_prices['timestamp'] = pd.to_datetime(df_prices['timestamp'], unit='ms')
    
    df_volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
    df_volumes['timestamp'] = pd.to_datetime(df_volumes['timestamp'], unit='ms')
    
    df_merged = pd.merge(df_prices, df_volumes, on='timestamp')
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = os.path.join(save_path, f'ethereum_raw_data.csv')
    df_merged.to_csv(filepath, index=False)
    print(f"Ethereum data saved to \n{filepath}\n\n")
    return filepath

if __name__ == "__main__":
    raw_data = fetch_ethereum_data()
    process_and_save(raw_data)