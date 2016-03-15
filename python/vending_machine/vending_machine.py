class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.coin_return = 0
        self.products = {"cola": 100, "chips": 50, "candy": 65}
        # self.products = {"cola": {'price': 100, 'quantity': 5}, "chips": 50, "candy": 65}
        self.display_message = ""

    def accept_coins(self, coin_input):
        valid_coins = [5, 10, 25]

        if coin_input == 1:
            self.coin_return += coin_input

        for coin in valid_coins:
            if coin_input == coin:
                self.amount += coin_input

    def select_product(self, product):
        price = self.products[product]

        if self.amount == price:
            self.amount -= price
            self.display_message = "THANK YOU"
        elif self.amount > price:
            self.coin_return += self.amount - price
        elif self.amount < price:
            self.display_message = "PRICE: %d" % price
            return
        return product

    def refund_coins(self):
        self.coin_return += self.amount
        self.amount = 0

    def return_coins(self):
        return self.coin_return

    def current_amount(self):
        return self.amount

    def display(self):
        if self.display_message:
            msg, self.display_message = self.display_message, ""
            return msg
        elif self.amount:
            self.display_message = "Current Amount: %d" % self.amount
        else:
            self.display_message = "INSERT COINS"

        return self.display_message
