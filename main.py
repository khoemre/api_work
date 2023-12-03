from requests import Request, Session
import pandas as pd
import os

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

api_key = '594b0fc3-4d4b-4bd7-b23e-c7bdc5d1325f'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
crypto =  response.json()['data']
#print(crypto)
#print(type(crypto))

'''
for i in crypto:
  print(f"id: {i['id']}, name: {i['name']}, last_update: {i['last_updated'].split('T')[0]}")
  print(f"Price: {i['quote']['USD']['price']}, one_day_changed: {i['quote']['USD']['percent_change_24h']}, one_week_changed: {i['quote']['USD']['percent_change_7d']}")
'''
#print(crypto)

data = pd.json_normalize(crypto)
#print(data)
#print(data.shape)
#print(data.info)
#print(data.head())
#print(data.columns)
#print(data['quote.USD.price'].value_counts())
#print(data.drop(['num_market_pairs'], axis=1))
data.to_csv(path_or_buf=r'C:\Users\TOSHIBA\OneDrive\Masaüstü/coin_market2.csv')




