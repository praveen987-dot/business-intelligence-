import smtplib
from email.mime.text import MIMEText
from utils.data_collection import fetch_ethereum_data, process_and_save
from utils.data_cleaning_ethereum import clean_ethereum_data
from utils.load_to_sqlite import load_to_sqlite
from utils.analyze_eth_data import analyze_eth_data
from utils.forecast_eth import forecast_eth_price

SENDER_EMAIL = "example@gmail.com"
RECEIVER_EMAIL = "example@gmail.com"
APP_PASSWORD = "your_app_password"

def send_failure_email(error_msg):
    subject = "ETL Pipeline Failed"
    body = f"Your ETL pipeline failed with the following error:\n\n{error_msg}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Failure notification sent.")
    except Exception as e:
        print("Error sending failure email:", e)

def run_etl():
    print("Starting ETL pipeline...")
    try:
        raw_data = fetch_ethereum_data()
        raw_data_filepath = process_and_save(raw_data)
        cleaned_data_filepath = clean_ethereum_data(raw_data_filepath)
        load_to_sqlite(cleaned_data_filepath)
        input_file_path = 'etl_project/data/ethereum_cleaned_data.csv'
        analyze_eth_data(input_file_path)
        forecast_eth_price(input_file_path)
        print("ETL pipeline completed successfully.")
    except Exception as e:
        error_msg = str(e)
        print("ETL pipeline failed:", error_msg)
        send_failure_email(error_msg)

if __name__ == "__main__":
    run_etl()
