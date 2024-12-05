import requests
import time
from datetime import datetime

BITCOIN_PRICE_THERSHOLD = 100000
BITCOIN_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
IFTTT_WEBHOOKS_URL = "https://maker.ifttt.com/trigger/{}/with/key/jApGvkFRotMI8bJ-Zqx_gr2ZIldgH7WV1AP9bwSDNuQ"


# Function to get the latest Bitcoin price from the API
def get_latest_bitcoin_price():
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "ebbbb9dc-6f8d-4fbc-aedd-17681f7cffe7"  # Replace with your actual API key
    }
    parameters = {"symbol": "BTC"}
    response = requests.get(BITCOIN_API_URL, headers=headers, params=parameters)
    response_json = response.json()
    btc_price = float(response_json["data"]["BTC"]["quote"]["USD"]["price"])
    return btc_price


# Function to send a POST request to IFTTT webhook
def post_ifttt_webhook(event, value):
    data = {'value1': value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)


# Function to format the Bitcoin price history for Telegram
def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = f"{date}: $<b>{price:,.4f}</b>"
        rows.append(row)
    return '<br>'.join(rows)


# Main function to handle the app logic
def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THERSHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', f"Bitcoin price dropped: ${price:,.4f}")

        # Send a Telegram Notification
        if len(bitcoin_history) == 5:
            formatted_message = format_bitcoin_history(bitcoin_history)
            post_ifttt_webhook('bitcoin_price_update', formatted_message)
            bitcoin_history = []  # Reset the history

        # Sleep for 5 minutes
        time.sleep(5 * 60)


if __name__ == '__main__':
    main()
