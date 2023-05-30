import json
import pandas as pd
import websocket
import base64
from ticker_pb2 import yaticker
import _thread as thread

from utils import refresh_excel_file, write_dataframe_to_excel

def on_message(ws, message):
    message = base64.b64decode(message)
    deserialized_data = yaticker()
    deserialized_data.ParseFromString(message)
    # Create a dictionary of data
    data = {
        'id': [deserialized_data.id],
        'price': [deserialized_data.price],
        'time': [deserialized_data.time],
        'currency': [deserialized_data.currency],
        'exchange': [deserialized_data.exchange],
        'quoteType': [deserialized_data.quoteType],
        'marketHours': [deserialized_data.marketHours],
        'changePercent': [deserialized_data.changePercent],
        'dayVolume': [deserialized_data.dayVolume],
        'dayHigh': [deserialized_data.dayHigh],
        'dayLow': [deserialized_data.dayLow],
        'change': [deserialized_data.change],
        'shortName': [deserialized_data.shortName],
        'expireDate': [deserialized_data.expireDate],
        'openPrice': [deserialized_data.openPrice],
        'previousClose': [deserialized_data.previousClose],
        'strikePrice': [deserialized_data.strikePrice],
        'underlyingSymbol': [deserialized_data.underlyingSymbol],
        'openInterest': [deserialized_data.openInterest],
        'optionsType': [deserialized_data.optionsType],
        'miniOption': [deserialized_data.miniOption],
        'lastSize': [deserialized_data.lastSize],
        'bid': [deserialized_data.bid],
        'bidSize': [deserialized_data.bidSize],
        'ask': [deserialized_data.ask],
        'askSize': [deserialized_data.askSize],
        'priceHint': [deserialized_data.priceHint],
        'vol_24hr': [deserialized_data.vol_24hr],
        'volAllCurrencies': [deserialized_data.volAllCurrencies],
        'fromcurrency': [deserialized_data.fromcurrency],
        'lastMarket': [deserialized_data.lastMarket],
        'circulatingSupply': [deserialized_data.circulatingSupply],
        'marketcap': [deserialized_data.marketcap]
    }

    # Create a DataFrame from the data dictionary
    df = pd.DataFrame(data)
    write_dataframe_to_excel(df, 'example.xlsx')
    # refresh_excel_file('example.xlsx')
# Rest of the WebSocket connection setup...


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    # Subscribe to a specific stock ticker for real-time data
    symbols = ["BTC-USD", "ETH-USD", "AAPL", "GOOGL"]
    symbols = json.dumps({"subscribe": symbols})
    def run():
        ws.send(symbols)
    thread.start_new_thread(run, ())

# Create a WebSocket connection to Yahoo Finance
websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://streamer.finance.yahoo.com/", 
                    on_message=on_message,
                    on_error=on_error,
                    on_close=on_close)
ws.on_open = on_open

# Start the WebSocket connection
ws.run_forever()
