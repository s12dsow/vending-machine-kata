class VendingMachine:
    def __init__(self):
        self.current_amount = 0
        self.coin_return = 0
        self.products = {"cola": 100, "chips": 50, "candy": 65}
        # self.products = {"cola": {'price': 100, 'quantity': 5}, "chips": 50, "candy": 65}
        self.display_message = "INSERT COINS"

    def accept_coins(self, coin_input):
        valid_coins = [5, 10, 25]

        if coin_input == 1:
            self.coin_return += coin_input
            return self.coin_return

        for coin in valid_coins:
            if coin_input == coin:
                self.current_amount += coin_input
                return self.current_amount

    def select_product(self, product):
        if self.current_amount == self.products[product]:
            self.current_amount -= self.products[product]
            self.display_message = "THANK YOU"
            return product
        elif self.current_amount > self.products[product]:
            self.coin_return += self.current_amount - self.products[product]
        elif self.current_amount < self.products[product]:
            self.display_message = "PRICE: %d" % self.products[product]

    def return_coins(self):
        self.coin_return += self.current_amount
        self.current_amount = 0

    def display(self):
        if self.display_message:
            msg, self.display_message = self.display_message, ""
            return msg
        elif self.current_amount:
            self.display_message = "Current Amount: %d" % self.current_amount
        else:
            self.display_message = "INSERT COINS"

        return self.display_message
