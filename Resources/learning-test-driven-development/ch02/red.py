import unittest

class Dollar:
    def __init__(self, amount):
        self.amount = amount 
    
    def times(self, multiplier):
        # return Dollar(5 * 2) ts: before abstraction
        return Dollar(self.amount * multiplier)
    

class TestMoney(unittest.TestCase):
    def testMultiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

        
    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros)
        self.assertEqual("EUR", twentyEuros.currency)


if __name__ == "__main__":
    unittest.main()