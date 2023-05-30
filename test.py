from ticker_pb2 import yaticker

message = b'\n\x04AAPL\x157\xd91C\x18\x80\xe5\x91\xcc\x8db*\x03NMS0\x088\x00Env\xb0?e\xc0\xc8\x1a@\xd8\x01\x04'


# Deserialize from bytes
deserialized_data = yaticker()
deserialized_data.ParseFromString(message)

print("Price:", deserialized_data.price)
print("Time:", deserialized_data.time)
print("Currency:", deserialized_data.currency)
print("Exchange:", deserialized_data.exchange)
# Access the OHLC data
open_price = deserialized_data.openPrice
high_price = deserialized_data.dayHigh
low_price = deserialized_data.dayLow
close_price = deserialized_data.price

# Print the OHLC data
print("Open Price:", open_price)
print("High Price:", high_price)
print("Low Price:", low_price)
print("Close Price:", close_price)
