# ETL Pipeline

This project is a complete end-to-end **ETL (Extract, Transform, Load)** pipeline built in Python for collecting, cleaning, storing, analyzing, and forecasting Ethereum cryptocurrency data using the CoinGecko API.

It also includes failure notification via email for enhanced monitoring.

## Features

- Collects Ethereum market data (last 365 days)
- Cleans and stores data in SQLite
- Generates key analysis plots (price/volume trends)
- Forecasts prices using a simple linear model
- Sends failure notifications via email
- Fully Windows-compatible (no Airflow/Docker)

## Setup and Implementaiton Instructions

### Step 1: Create a Virtual Environment
Open Command Prompt (cmd) or PowerShell and run:
 
    python -m venv venv

This will create a virtual environment named venv in your project folder.

### Step 2: Activate the Virtual Environment

    venv\Scripts\activate

After activation, your terminal should show a prefix like (venv) indicating that the virtual environment is active.

### Step 3: Install Required Packages
Make sure you are in the root of the project directory (where requirements.txt is located), then run:

    pip install -r requirements.txt

This will install all necessary dependencies

### Step 4: Navigate to the Project Directory

If you're not already in your project folder, navigate to it:

    cd path\to\your\etl_project

### Step 5: Run the ETL Pipeline

    python etl_pipeline.py

This script performs the complete ETL process:

- Fetches Ethereum market data from CoinGecko
- Cleans and stores the data in a local SQLite database
- Generates multiple graphs and stores them
- Applies a simple forecasting model
- Sends an email notification if the pipeline fails


## Project Folder Structure

etl_project/
│
├── etl_pipeline.py                # To run the pipeline
├── requirements.txt               # All required Python packages
├── data/                          # Stores raw, cleaned CSVs and plots
│   ├── ethereum_raw_data.csv
│   ├── ethereum_cleaned_data.csv
|   ├── ethereum.db
│   ├── analysis/
│   │   ├── eth_daily_pct_change.png
│   │   ├── eth_price_moving_average.png
│   │   ├── eth_price_over_time.png
│   │   ├── eth_volume_histogram.png
│   │   └── eth_volume_over_time.png
│   ├── forecasted/
│   │   └── eth_price_forecast.png
├── utils/                         # All helper modules
│   ├── data_collection.py         # Fetch + save raw ETH data
│   ├── data_cleaning_ethereum.py  # Clean and format data
│   ├── load_to_sqlite.py          # Load to SQLite database
│   ├── analyze_eth_data.py        # Generate and save plots
│   └── forecast_eth.py            # Simple forecasting
