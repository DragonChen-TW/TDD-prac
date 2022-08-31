import functools
import operator
# 
from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._EURToUSD = 1.2
    
    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency):
        total = 0
        for m in self.moneys:
            total += m.amount
        total = functools.reduce(
            operator.add,
            [self.__convert(m, currency) for m in self.moneys],
            0
        )
        return Money(total, currency)
    
    def __convert(self, money, currency):
        if money.currency == currency:
            return money.amount
        else:
            return money.amount * self._EURToUSD