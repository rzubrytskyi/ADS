shares = [
{"name": "AAPL", "price": 150},
{"name": "GOOGL", "price": 2800},
{"name": "TSLA", "price": 700},
{"name": "AMZN", "price": None},
]

def average_portfolio_value(shares, min_price=None, max_price=None):
    total_value = 0
    count = 0
    for share in shares:
        price = share.get("price")
        if price is None:
            continue
        if (min_price is not None and price < min_price) or (max_price is not None and price > max_price):
            continue
        total_value += price
        count += 1
    if count == 0:
        return "No valid prices available"
    average_value = total_value / count
    return average_value

print(average_portfolio_value(shares, min_price=50, max_price=2500))