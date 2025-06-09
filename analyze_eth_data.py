import os
import pandas as pd
import matplotlib.pyplot as plt

def analyze_eth_data(input_csv, output_dir = 'etl_project/data/analysis'):
    df = pd.read_csv(input_csv, parse_dates=['timestamp'])
    df.rename(columns={'timestamp': 'date'}, inplace=True)

    os.makedirs(output_dir, exist_ok=True)

    # Plot 1: Ethereum Price Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['price'], label='ETH Price (USD)', color='blue')
    plt.title("Ethereum Price Over Last 365 Days")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/eth_price_over_time.png")
    plt.close()

    # Plot 2: Ethereum Trading Volume Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['volume'], label='Volume', color='green')
    plt.title("Ethereum Trading Volume Over Last 365 Days")
    plt.xlabel("Date")
    plt.ylabel("Volume (USD)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/eth_volume_over_time.png")
    plt.close()

    # Plot 3: 30-Day Moving Average of Price
    df['price_ma_30'] = df['price'].rolling(window=30).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['price'], label='ETH Price', alpha=0.5)
    plt.plot(df['date'], df['price_ma_30'], label='30-Day MA', color='red')
    plt.title("Ethereum Price with 30-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/eth_price_moving_average.png")
    plt.close()

    # Plot 4: Volume Distribution Histogram
    plt.figure(figsize=(12, 6))
    plt.hist(df['volume'], bins=50, color='purple')
    plt.title("Distribution of Daily Ethereum Trading Volume")
    plt.xlabel("Volume (USD)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/eth_volume_histogram.png")
    plt.close()

    # Plot 5: Daily Price Change Percentage
    df['price_change_pct'] = df['price'].pct_change() * 100
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['price_change_pct'], color='orange')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("Daily Percentage Change in Ethereum Price")
    plt.xlabel("Date")
    plt.ylabel("Percent Change (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/eth_daily_pct_change.png")
    plt.close()

    print(f"Ethereum data analysis completed. Plots saved to: \n{output_dir}\n\n")

if __name__ == "__main__":
    input_file_path = 'etl_project/data/ethereum_cleaned_data.csv'
    analyze_eth_data(input_file_path)
