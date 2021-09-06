class Coin:

    def __init__(self, symbol, name, price_usd):
        self.symbol = symbol
        self.name = name
        self.price_usd = price_usd

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_price_usd(self):
        return self.price_usd

    def to_string(self):
        print("Coin(" + self.symbol + ", " + self.name + ", " + self.price_usd + ")")
