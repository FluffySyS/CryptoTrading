from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from time import sleep
from datetime import datetime
import os
path = f"{os.getcwd()}"
with open(f"{path}\\api_key.txt", 'r') as api_file:
    lines = api_file.readlines()[0].rstrip('\n')
api_key_1 = lines.split(',')[0]
api_key_2 = lines.split(',')[1]
client = Client(api_key_1, api_key_2)



while client.get_symbol_info("LUNABUSD")['status'] == 'BREAK':
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S:%f")[:-3]
    print(f"[{current_time}] {'LUNA not available yet.'}")

# print(client.get_ticker(symbol="LTCBUSD"))
while True:
    try:
        buy_order = client.order_market_buy(
                    symbol="LUNABUSD",
                    quoteOrderQty=300.00,
                )
        break
    except:
        continue
print(buy_order)
price_bought = buy_order['fills'][0]['price']
luna_quantity = round(float(buy_order['executedQty']),3)
luna_quantity_a = round((luna_quantity/4),3)

current_price = client.get_ticker(symbol="LUNABUSD")['lastPrice']

def sell_order():
    try:
        sell_order = client.order_market_sell(
            symbol="LUNABUSD",
            quantity=luna_quantity_a,
            )
    except Exception as e:
        print(e)
    try:
        print(sell_order)
    except Exception as e:
        print(e)


while current_price < price_bought * 5:
    current_price = client.get_ticker(symbol="LUNABUSD")['lastPrice']
sell_order()

while current_price < price_bought * 10:
    current_price = client.get_ticker(symbol="LUNABUSD")['lastPrice']
sell_order()

while current_price < price_bought * 20:
    current_price = client.get_ticker(symbol="LUNABUSD")['lastPrice']
sell_order()
# print(client.get_ticker(symbol="LUNABUSD"))
