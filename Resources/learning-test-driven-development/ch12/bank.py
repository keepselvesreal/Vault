from money import Money


class Bank:
    def __init__(self):
        self.exchageRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchageRates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)
        
        key = aMoney.currency + "->" + aCurrency
        if key in self.exchageRates:
            return Money(aMoney.amount * self.exchageRates[key], aCurrency)
        # raise  Exception("Faild")
        raise Exception(key)




    