import functools
import operator

from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_end = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self._convert(m, currency), self.moneys), 0
            )
        return Money(total, currency)

    def _convert(self, aMoney, aCurrency):
        # exchangeRates = {}
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency + "->" + aCurrency
            return aMoney.amount * exchangeRates[key]