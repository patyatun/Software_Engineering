import unittest

def calculate_tea_cost(yuzu_qty, mint_ginger_qty):
    return round((yuzu_qty * 3.5) + (mint_ginger_qty * 3.5), 2)

def calculate_noncoffee_cost(chocolate_qty, matcha_latte_qty):
    return round((chocolate_qty * 4) + (matcha_latte_qty * 4.5), 2)

def calculate_coffee_cost(espresso_qty, double_espresso_qty):
    return round((espresso_qty * 2) + (double_espresso_qty * 3), 2)

def calculate_subtotal(varTeaCost, varNoncoffeeCost, varCoffeeCost):
    return round(varTeaCost + varNoncoffeeCost + varCoffeeCost, 2)

def calculate_iva(subtotal):
    return round(subtotal * 0.16, 2)

def calculate_total(subtotal, iva):
    return round(subtotal + iva, 2)

#unit tests

class TestCoffeeCalculations(unittest.TestCase):

    def test_calculate_tea_cost(self):
        self.assertEqual(calculate_tea_cost(1, 1), 7.0)
        self.assertEqual(calculate_tea_cost(0, 2), 7.0)
        self.assertEqual(calculate_tea_cost(3, 0), 10.5)
        self.assertEqual(calculate_tea_cost(0, 0), 0.0)

    def test_calculate_noncoffee_cost(self):
        self.assertEqual(calculate_noncoffee_cost(1, 1), 8.5)
        self.assertEqual(calculate_noncoffee_cost(2, 0), 8.0)
        self.assertEqual(calculate_noncoffee_cost(0, 2), 9.0)
        self.assertEqual(calculate_noncoffee_cost(0, 0), 0.0)

    def test_calculate_coffee_cost(self):
        self.assertEqual(calculate_coffee_cost(1, 1), 5.0)
        self.assertEqual(calculate_coffee_cost(2, 0), 4.0)
        self.assertEqual(calculate_coffee_cost(0, 2), 6.0)
        self.assertEqual(calculate_coffee_cost(0, 0), 0.0)

    def test_calculate_subtotal(self):
        self.assertEqual(calculate_subtotal(7.0, 8.5, 5.0), 20.5)
        self.assertEqual(calculate_subtotal(0.0, 0.0, 0.0), 0.0)
        self.assertEqual(calculate_subtotal(3.5, 4.5, 2.0), 10.0)
        self.assertEqual(calculate_subtotal(7.0, 7.0, 7.0), 21.0)

    def test_calculate_iva(self):
        self.assertEqual(calculate_iva(20.5), 3.28)
        self.assertEqual(calculate_iva(0.0), 0.0)
        self.assertEqual(calculate_iva(10.0), 1.6)
        self.assertEqual(calculate_iva(21.0), 3.36)

    def test_calculate_total(self):
        self.assertEqual(calculate_total(20.5, 3.28), 23.78)
        self.assertEqual(calculate_total(0.0, 0.0), 0.0)
        self.assertEqual(calculate_total(10.0, 1.6), 11.6)
        self.assertEqual(calculate_total(21.0, 3.36), 24.36)

if __name__ == '__main__':
    unittest.main()