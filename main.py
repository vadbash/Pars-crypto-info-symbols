from twelvedata import TDClient
from pprint import pprint
import csv

#Your api key
apikey = "Your_api_key"

# Read the list of symbols from the CSV file
symbols = []
with open('symbols.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        symbols.extend(row)

# Function that apply symbols and api key
def get_time_series(symbol, interval):
    td = TDClient(apikey=apikey)
    ts = td.time_series(
        symbol=symbol,
        interval=interval,
    )
    return ts.as_json()

# Intervals
intervals = ["1min", "5min", "15min", "30min", "45min", "1h", "2h", "4h", "1day", "1week", "1month"]
# File where data will be write
csv_file = "data.csv"

# Main function
for symbol in symbols:
    for interval in intervals:
        print(f"Processing data for symbol: {symbol} with interval: {interval}")
        data = get_time_series(symbol, interval)

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')

            if file.tell() == 0:
                # Write header only if the file is empty
                writer.writerow(['symbol', 'datetime', 'open', 'high', 'low', 'close'])

            for entry in data:
                row = [symbol, entry['datetime'], entry['open'], entry['high'], entry['low'], entry['close']]
                writer.writerow(row)

print("Data processing completed.")