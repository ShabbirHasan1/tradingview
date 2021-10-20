from tradingview.client import TradingViewWebSocketClient, fetch_japan_symbols
from datetime import datetime

client = TradingViewWebSocketClient()

symbols = fetch_japan_symbols()
client.add_symbols(symbols[:100])
# client.add_symbols(['TSE:4689'])

for x in client.fetch_ohlc(past_bar=302):
    print(datetime.fromtimestamp(x.bar_time), x)