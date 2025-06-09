import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta
import os

def forecast_eth_price(input_path, output_dir='etl_project/data/forecasted/', forecast_days=30):
    df = pd.read_csv(input_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    df['days_since_start'] = (df['timestamp'] - df['timestamp'].min()).dt.days
    X = df[['days_since_start']]
    y = df['price']

    model = LinearRegression()
    model.fit(X, y)

    last_day = df['days_since_start'].max()
    future_days = pd.DataFrame({'days_since_start': [last_day + i for i in range(1, forecast_days + 1)]})
    future_prices = model.predict(future_days)

    future_dates = [df['timestamp'].max() + timedelta(days=i) for i in range(1, forecast_days + 1)]

    forecast_df = pd.DataFrame({
            'timestamp': future_dates,
            'predicted_price': future_prices
        })

    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['price'], label='Historical Price')
    plt.plot(forecast_df['timestamp'], forecast_df['predicted_price'], label='Forecasted Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('ETH Price (USD)')
    plt.title('Ethereum Price Forecast (Simple Linear Regression)')
    plt.legend()
    plt.grid(True)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'eth_price_forecast.png')
    plt.savefig(output_path)
    print(f"Forecast graph saved to: \n{output_path}\n\n")

if __name__ == "__main__":
    forecast_eth_price()
