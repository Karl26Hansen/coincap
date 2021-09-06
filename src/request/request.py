import json
from decimal import Decimal
from datetime import datetime
from conf.conf import API_URL

from coin.coin import Coin
import requests


def get_data():
    response = requests.get(API_URL)
    if response.ok:
        parsed = str(response.json()).replace("'", "\"").replace("None", 'null')
        return json.loads(parsed)
    else:
        return response


def get_datetime_in_seconds(timestamp):
    date = str(datetime.fromtimestamp(timestamp).date()).replace("-", "_")
    time = str(datetime.fromtimestamp(timestamp).time()).split(".")[0].replace(":", "_")
    return date + "_" + time


def display_coin_data(json_data):
    coin_data = json_data
    coin_list = coin_data['data']

    top_coins = []
    for coin in coin_list:
        symbol = coin['symbol']
        name = coin['name']
        price_usd_raw = Decimal(coin['priceUsd'])
        price_usd = round(price_usd_raw, 3)
        if int(coin['rank']) <= 50:
            top_coins.append(Coin(symbol, name, str(price_usd)))
        else:
            break

    return top_coins
