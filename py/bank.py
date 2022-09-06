from money import Money

class Bank:
    def __init__(self):
        self.exchangeRates = {}
    
    def addExchangeRate(self, fromCurrency: str, toCurrency: str, rate: float) -> None:
        key = f'{fromCurrency}->{toCurrency}'
        self.exchangeRates[key] = rate
    
    def convert(self, money: Money, currency: str) -> Money:
        if money.currency == currency:
            return money
        
        key = f'{money.currency}->{currency}'
        if key not in self.exchangeRates:
            raise Exception(key)
        
        rate = self.exchangeRates[key]
        return Money(money.amount * rate, currency)