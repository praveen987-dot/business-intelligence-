import pandas as pd
import sqlite3
import os

def load_to_sqlite(cleaned_csv_path, db_path='etl_project/data/ethereum.db'):
    df = pd.read_csv(cleaned_csv_path)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ethereum_market_data (
            timestamp TEXT PRIMARY KEY,
            price REAL,
            volume REAL
        )
    ''')

    df.to_sql('ethereum_market_data', conn, if_exists='append', index=False)
    print(f"Data inserted into SQLite database at \n{db_path}\n\n")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    cleaned_path = 'etl_project/data/ethereum_cleaned_data.csv'
    load_to_sqlite(cleaned_path)
