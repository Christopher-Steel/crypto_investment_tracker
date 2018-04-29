import json
import requests

# paid = 100
# owned = 0.01243852

url = "https://api.coinbase.com/v2/exchange-rates?currency="

currencies = [
    ["BTC", 100, 0.01243852],
    ["ETH", 158.33 + 128.58, 0.25 + 0.20275813],
    ["LTC", 89.08, 0.56375339]
]

total_value = 0
total_difference = 0

for [currency, paid, owned] in currencies:
    res = requests.get(url + currency).json()

    current_price = float(res["data"]["rates"]["GBP"])
    current_value = current_price * owned
    difference = current_value - float(paid)

    total_value += current_value
    total_difference += difference

    print("-------- %s --------" % currency)
    print("Difference:      %.2f" % difference)
    print("current value:   %.2f" % current_value)
    print("current_price:   %.2f" % current_price)
    print("")

print("________ TOTAL ________")
print("Difference:   %.2f" % total_difference)
print("Value:        %.2f" % total_value)
