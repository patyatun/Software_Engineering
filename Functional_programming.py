# Higher-Order Functions
def apply_discount(discount_func, price):
    return discount_func(price)

def student_discount(price):
    return price * 0.8  # 20% discount

def senior_discount(price):
    return price * 0.9  # 10% discount

# Functions as Parameters and Return Values
def calculate_total(items, discount_func=None):
    total = sum(item.price for item in items)
    if discount_func:
        total = apply_discount(discount_func, total)
    return total

# Closures / Anonymous Functions
def create_discount_func(discount_rate):
    return lambda price: price * (1 - discount_rate)

# Only Final Structures
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price}"

# (Mostly) Side-Effect-Free Functions
def filter_menu(menu, category):
    return [item for item in menu if category in item.name.lower()]

def sort_menu(menu, reverse=False):
    return sorted(menu, key=lambda item: item.price, reverse=reverse)

# Example Usage
menu = [
    MenuItem("Espresso", 2.0),
    MenuItem("Cappuccino", 3.5),
    MenuItem("Latte", 3.8),
    MenuItem("Matcha Latte", 4.5),
    MenuItem("Yuzu Tea", 3.5),
    MenuItem("Jujube Goji Tea", 3.8),
]

# Filter and sort the menu
coffee_menu = filter_menu(menu, "coffee")
sorted_coffee_menu = sort_menu(coffee_menu, reverse=True)
print("Sorted Coffee Menu:")
for item in sorted_coffee_menu:
    print(item)

# Calculate total with discounts
order = [menu[0], menu[2], menu[4]]
regular_total = calculate_total(order)
print(f"\nRegular Total: ${regular_total}")

student_discount_func = create_discount_func(0.2)
student_total = calculate_total(order, student_discount_func)
print(f"Student Total: ${student_total}")

senior_total = calculate_total(order, senior_discount)
print(f"Senior Total: ${senior_total}")
