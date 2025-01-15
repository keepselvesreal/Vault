class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency) # self.amount * multiplier 부분은 이전에 이미 이에 대한 abstraction 진행을 설명한 적 있음

    def divide(self, divisor):
        return Money(self.amount / divisor,  self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    
    def __str__(self):
        return f"{self.currency} {self.amount:0.2f}"