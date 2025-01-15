import functools
import operator

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_end = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, bank, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)
        
        if len(failures) == 0:
            return Money(total, currency) # 기존 evaluate 반환 결과
        
        # failureMessage = ",".join(str(f) for f in failures)
        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")

    def _convert(self, aMoney, aCurrency):
        # exchangeRates = {}
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency + "->" + aCurrency
            return aMoney.amount * exchangeRates[key]