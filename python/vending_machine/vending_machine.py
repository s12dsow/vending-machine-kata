class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.coin_return = 0
        self.products = {"cola": {'price': 100, 'quantity': 5},
                         "chips": {'price': 50, 'quantity': 10},
                         "candy": {'price': 65, 'quantity': 10}}
        self.display_message = ""
        self.change = {"quarters": 5, "dimes": 10, "nickels": 10}

    def accept_coins(self, coin_input):
        valid_coins = [5, 10, 25]

        if coin_input == 1:
            self.coin_return += coin_input

        for coin in valid_coins:
            if coin_input == coin:
                self.amount += coin_input

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
            elif self.amount < price:
                self.display_message = "PRICE: %d" % price
                return
            return product
        else:
            self.display_message = "SOLD OUT"

    def refund_coins(self):
        self.coin_return += self.amount
        self.amount = 0

    def return_coins(self):
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
