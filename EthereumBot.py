import requests
import time
import config
from datetime import datetime

while True:
  coinmarket_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

  parameters = {
      'start': '1',
      'limit': '5000',
      'convert': 'CAD'
  }
  headers = {
      'Accepts': 'application/json',
      # Remove "config.coinmarket_api" and put YOUR CoinMarketCap API key there.
      'X-CMC_PRO_API_KEY': config.coinmarket_api,
  }

  print('Sending Request')
  response = requests.get(coinmarket_url, params=parameters, headers=headers)
  response_json = response.json()

  print("Got Response")
  # Ethereum data is the second element on the list.
  ether_data = response_json['data'][1]
  price_cad = str(ether_data['quote']['CAD']['price'])

  def main():

      ## Change "config.Etherr_Bot_api" and "config.chat_id" to YOUR Telegram Bot API and Chat ID
      Telegram_url = ("https://api.telegram.org/bot" + config.Etherr_Bot_api + "/sendMessage?chat_id=-" + config.chat_id + "&text=Ethereum Price is " + price_cad + " CAD")

      requests.get(Telegram_url)
      time.sleep(600) ## Sleep for 10 minutes

  if __name__ == '__main__':
      main()
