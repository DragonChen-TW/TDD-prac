import unittest
# 
from money import Money
from portfolio import Portfolio
from bank import Bank

class TestMoney(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.addExchangeRate('EUR', 'USD', 1.2)
        self.bank.addExchangeRate('USD', 'KRW', 1100)

    def testMultiplication(self):
        tenEuros = Money(10, 'EUR')
        twentyEuros = Money(20, 'EUR')
        self.assertEqual(twentyEuros, tenEuros.times(2))
    
    def testDivision(self):
        originalMoney = Money(4002, 'KRW')
        dividedMoney = Money(1000.5, 'KRW')
        self.assertEqual(dividedMoney, originalMoney.divide(4))

    def testAddition(self):
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        fifteenDollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate(self.bank, 'USD'))
    
    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, 'USD')
        tenEuros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, 'USD')
        actualValue = portfolio.evaluate(self.bank, 'USD')
        self.assertEqual(expectedValue, actualValue,
            f'{expectedValue} != {actualValue}')

    def testAdditionOfDollarsAndWons(self):
        oneDollar = Money(1, 'USD')
        elevenHundredWon = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, 'KRW')
        actualValue = portfolio.evaluate(self.bank, 'KRW')
        self.assertEqual(expectedValue, actualValue,
            f'{expectedValue} != {actualValue}')
    
    def testAdditionWithMultipleMissingExchangeRates(self):
        oneDollar = Money(1, 'USD')
        oneEuro = Money(1, 'EUR')
        oneWon = Money(1, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
            Exception,
            'Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]',
        ):
            portfolio.evaluate(self.bank, 'Kalganid')
    
    def testConversion(self):
        tenEuros = Money(10, 'EUR')
        expectedMoney = Money(12, 'USD')
        self.assertEqual(expectedMoney, self.bank.convert(tenEuros, 'USD'))

    def testConversionWithMissingExchangeRate(self):
        tenEuros = Money(10, 'EUR')
        with self.assertRaisesRegex(Exception, 'EUR->Kalganid'):
            self.bank.convert(tenEuros, 'Kalganid')

if __name__ == '__main__':
    unittest.main()