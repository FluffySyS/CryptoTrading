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

    current_time = now.strftime("%H:%M:%S")
    print(f"[{current_time}] {'LUNA not available yet.'}")
    sleep(0.1)

# print(client.get_ticker(symbol="LTCBUSD"))
while True:
    try:
        buy_order = client.order_market_buy(
                    symbol="LUNABUSD",
                    quoteOrderQty=13.00,
                )
        break
    except:
        continue
print(buy_order)
price_bought = buy_order['fills'][0]['price']
luna_quantity = buy_order['executedQty']

while True:
    current_price = client.get_ticker(symbol="LUNABUSD")['lastPrice']
    if current_price <= (price_bought - (price_bought * 0.3)) or current_price >= price_bought * 20:
        try:
            sell_order = client.order_market_sell(
                symbol="LUNABUSD",
                quoteOrderQty=luna_quantity,
                )
            break
        except:
            continue
print(sell_order)
# print(client.get_ticker(symbol="LUNABUSD"))