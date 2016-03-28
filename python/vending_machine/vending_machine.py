class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.coin_return = 0
        self.display_message = ""
        self.products = {"cola": {'price': 100, 'quantity': 5},
                         "chips": {'price': 50, 'quantity': 10},
                         "candy": {'price': 65, 'quantity': 10}}
        self.change = {"quarters": {'value': 25, 'quantity': 5},
                       "dimes": {'value': 10, 'quantity': 10},
                       "nickels": {'value': 5, 'quantity': 10}}

    def current_amount(self):
        return self.amount

    def accept_coins(self, coin_input):
        if coin_input == 1:
            self.coin_return += coin_input
        else:
            converter = {25: "quarters", 10: "dimes", 5: "nickels"}
            coin = converter[coin_input]
            coin_value = self.change[coin]['value']

            if coin_input == coin_value:
                self.amount += coin_input
                self.change[coin]['quantity'] += 1

    def select_product(self, product):
        price = self.products[product]['price']
        quantity = self.products[product]['quantity']

        if self.can_make_change():
            if quantity:
                if self.amount == price:
                    self.amount -= price
                    self.products[product]['quantity'] -= 1
                    self.display_message = "THANK YOU"
                elif self.amount > price:
                    self.amount -= price
                    self.products[product]['quantity'] -= 1
                else:
                    self.display_message = "PRICE: %d" % price
                    return
                return product
            else:
                self.display_message = "SOLD OUT"
        else:
            self.display_message = "EXACT CHANGE ONLY"

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


class CoinDetector:
    def __init__(self, weight, diameter, thickness):
        self.weight = weight
        self.diameter = diameter
        self.thickness = thickness

    def identify_coin(self):
        if self.weight == 5.670 and self.diameter == 24.26 and self.thickness == 1.75:
            return "quarter"
        elif self.weight == 2.268 and self.diameter == 17.91 and self.thickness == 1.35:
            return "dime"
        elif self.weight == 5.000 and self.diameter == 21.21 and self.thickness == 1.95:
            return "nickel"
        else:
            return "INVALID"


