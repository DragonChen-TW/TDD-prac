import functools
import operator
# 
from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
    
    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency):
        total = 0
        failures = []

        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke: # there is no matched conversion
                failures.append(str(ke.args[0]))

        if len(failures) > 0: # there is an error
            failureMessage = ','.join(failures)
            raise Exception(f"Missing exchange rate(s):[{failureMessage}]")

        return Money(total, currency)
    
    def __convert(self, money, currency):
        if money.currency == currency:
            return money.amount

        exchangeRates = {
            'EUR->USD': 1.2,
            'USD->KRW': 1100,
        }

        key = f'{money.currency}->{currency}'
        return money.amount * exchangeRates[key]