import re

# DSL Grammar Definition
grammar = {
    'order': r'Order:\s*(?P<orders>.*)',
    'order_item': r'(?P<quantity>\d+)\s*(?P<product_type>Tea|Non-Coffee|Coffee)',
    'product_types': {
        'Tea': 3.5,
        'Non-Coffee': 4.5,
        'Coffee': 3.0
    }
}

# Function to parse an order
def parse_order(order_str):
    order_pattern = re.compile(grammar['order'], re.IGNORECASE)
    order_match = order_pattern.match(order_str)
    if not order_match:
        return None

    orders = order_match.group('orders')
    order_item_pattern = re.compile(grammar['order_item'])
    total = 0
    for item in order_item_pattern.finditer(orders):
        quantity = int(item.group('quantity'))
        product_type = item.group('product_type')
        price = grammar['product_types'][product_type]
        total += quantity * price

    return total

# Example usage
order1 = "Order: 2 Tea 1 Non-Coffee 3 Coffee"
total1 = parse_order(order1)
print(f"Total to pay: ${total1}")

order2 = "Order: 5 Tea 2 Non-Coffee 1 Coffee"
total2 = parse_order(order2)
print(f"Total to pay: ${total2}")
