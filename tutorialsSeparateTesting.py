import requests

#defining API endpoint
bitcoin_api_url = "https://pro-api.coinmarketcap.com/cryptocurrency/latest/"

#Query parameters
parameters = {
	"symbol": "BTC"
	}

#Headers including the API key
headers = {
	"Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "ebbbb9dc-6f8d-4fbc-aedd-17681f7cffe7"  # Replace with your actual API key
}

response = requests.get(bitcoin_api_url, headers=headers, params=parameters)
response_json = response.json()
type(response_json)
print(response_json)

#structure response
btc_price = response_json["data"]["BTC"]["quote"]["USD"]["price"]
btc_volume = response_json["data"]["BTC"]["quote"]["USD"]["volume_24h"]
btc_market_cap = response_json["data"]["BTC"]["quote"]["USD"]["market_cap"]

#Print the details
print(f"Bitcoin Price: ${btc_price:,.2f}")
print(f"24-Hour Volume: ${btc_volume:,.2f}")
print(f"Market Cap: ${btc_market_cap:,.2f}")


ebbbb9dc-6f8d-4fbc-aedd-17681f7cffe7 -  coinmarket



IFTTTT

import requests

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/json/with/key/jApGvkFRotMI8bJ-Zqx_gr2ZIldgH7WV1AP9bwSDNuQ'
requests.post(ifttt_webhook_url)


ALL TOGETHER
import requests
import time
from datetime import datetime

def main():
    pass
    
if __name__ == '__main__':
    main()
