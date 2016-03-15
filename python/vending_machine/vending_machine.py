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

        if quantity:
            if self.amount == price:
                self.amount -= price
                self.products[product]['quantity'] -= 1
                self.display_message = "THANK YOU"
            elif self.amount > price:
                self.coin_return += self.amount - price
                self.products[product]['quantity'] -= 1
            else:
                self.display_message = "PRICE: %d" % price
                return
            return product
        else:
            self.display_message = "SOLD OUT"

    def refund_coins(self):
        self.coin_return += self.amount
        self.amount = 0

    def return_coins(self):
        if self.make_change():
            return self.coin_return

    def current_amount(self):
        return self.amount

    def make_change(self):
        return self.change['dimes'] > 1 and self.change['nickels'] > 1 \
               or self.change['nickels'] > 3

    def display(self):
        if self.display_message:
            msg, self.display_message = self.display_message, ""
            return msg
        elif not self.make_change():
            self.display_message = "EXACT CHANGE ONLY"
        elif self.amount:
            self.display_message = "Current Amount: %d" % self.amount
        else:
            self.display_message = "INSERT COINS"

        return self.display_message
