class VendingMachine:
    def __init__(self, products=None):
        self.amount = 0
        self.coin_return = 0
        self.display_message = ""
        if not products:
            products = [Product("cola", 100, 1), Product("chips", 50, 5), Product("candy", 65, 7)]
        self.products = products
        self.coin_detector = CoinDetector([Coin(5.670, 24.26, 1.75, 25),
                                           Coin(2.268, 17.91, 1.35, 10),
                                           Coin(5.000, 21.21, 1.95, 5)])

    def current_amount(self):
        return self.amount

    def insert_coin(self, coin_value):
        for coin in self.coin_detector.valid_coins:
            if coin_value == coin.value:
                self.amount += coin_value
                break
        else:
            self.coin_return += coin_value

    def select_product(self, product):
        for item in self.products:
            if item.name == product:
                if item.quantity > 0:
                    if self.amount >= item.price:
                        self.amount -= item.price
                        self.coin_return += self.amount
                        item.quantity -= 1
                        self.display_message = "THANK YOU"
                        return item.name
                    else:
                        self.display_message = "PRICE: %d" % item.price
                else:
                    self.display_message = "SOLD OUT"

    def return_coins(self):
        value = self.amount
        self.amount = 0

        return CoinReturn([Coin(5.670, 24.26, 1.75, 25),
                           Coin(2.268, 17.91, 1.35, 10),
                           Coin(5.000, 21.21, 1.95, 5)]).return_coins(value)

    def can_make_change(self):
        return self.change['dimes'] > 1 and self.change['nickels'] > 1 \
               or self.change['nickels'] > 3

    def refund_coins(self):
        self.coin_return += self.amount
        self.amount = 0

    def update_coin_inventory_when_refunding(self):
        value = self.coin_return

        while value > 1:
            if value >= 25:
                if self.change['quarters']['quantity']:
                    value -= 25
                    self.change['quarters']['quantity'] -= 1
            if 10 <= value < 25:
                if self.change['dimes']['quantity']:
                    value -= 10
                    self.change['dimes']['quantity'] -= 1
            if 5 <= value < 10:
                if self.change['nickels']['quantity']:
                    value -= 5
                    self.change['dimes']['quantity'] -= 1
        return self.coin_return

    def display(self):
        if self.display_message:
            msg, self.display_message = self.display_message, ""
            return msg
        elif self.amount:
            self.display_message = "Current Amount: %d" % self.amount
        else:
            self.display_message = "INSERT COINS"

        return self.display_message


class Coin:
    def __init__(self, weight, diameter, thickness, value=None):
        self.weight = weight
        self.diameter = diameter
        self.thickness = thickness
        self.value = value

    def __repr__(self):
        return "<Coin:%s>" % self.value

    def __eq__(self, other):
        return self.weight == other.weight and self.diameter == other.diameter and self.thickness == other.thickness


class CoinDetector(object):
    def __init__(self, valid_coins=[]):
        self.valid_coins = valid_coins

    def identify_coin(self, coin):
        for valid_coin in self.valid_coins:
            if coin == valid_coin:
                value = valid_coin.value
                break
        else:
            value = 0
        return value


class CoinReturn(CoinDetector):
    def __init__(self, valid_coins=[]):
        super(CoinReturn, self).__init__(valid_coins)

    def return_coins(self, value):
        return_coins = []
        while value > 0:
            for valid_coin in self.valid_coins:
                while valid_coin.value <= value:
                    return_coins.append(valid_coin)
                    value -= valid_coin.value
        return return_coins


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
