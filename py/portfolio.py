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
        for m in self.moneys:
            total += m.amount
        total = functools.reduce(
            operator.add,
            [m.amount for m in self.moneys],
            0
        )
        return Money(total, currency)