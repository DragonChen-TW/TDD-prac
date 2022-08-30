import unittest
import functools
import operator

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

class Profolio:
    def __init__(self):
        self.moneys = []
    
    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency):
        total = 0
        for m in self.moneys:
            total += m.amount
        total = functools.reduce(
            operator.add,
            [m.amount for m in self.moneys],
            0
        )
        return Money(total, currency)

class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))
    
    def testMultiplicationEuros(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = Money(20, 'EUR')
        self.assertEqual(twentyEuros, tenEuros.times(2))
    
    def testDivision(self):
        originalMoney = Money(4002, 'KRW')
        dividedMoney = Money(1000.5, 'KRW')
        self.assertEqual(dividedMoney, originalMoney.divide(4))

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        profolio = Profolio()
        profolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, profolio.evaluate('USD'))

if __name__ == '__main__':
    unittest.main()