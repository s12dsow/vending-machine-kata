import unittest
from vending_machine.vending_machine import VendingMachine, CoinDetector, Coin, Product, CoinReturn


class TestVendingMachine(unittest.TestCase):
    """Tests for vending machine"""
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_vending_machine_insert_quarters(self):
        """should accept valid coins"""
        self.vending_machine.insert_coin(25)

        self.assertEqual(self.vending_machine.display(), "Current Amount: 25")

    def test_vending_machine_accepts_dimes(self):
        """should accept valid coins"""
        self.vending_machine.insert_coin(10)

        self.assertEqual(self.vending_machine.display(), "Current Amount: 10")

    def test_vending_machine_accepts_nickels(self):
        """should accept valid coins"""
        self.vending_machine.insert_coin(5)

        self.assertEqual(self.vending_machine.display(), "Current Amount: 5")

    def test_vending_machine_rejects_pennies_and_returns_them(self):
        """should reject and put pennies in coin return"""

        self.vending_machine.insert_coin(1)

        self.assertEqual(self.vending_machine.display(), "INSERT COINS")
        self.assertEqual(self.vending_machine.coin_return, 1)

    def test_vending_machine_updates_display_when_valid_coin_accepted(self):
        """should update display when received valid coin"""
        self.vending_machine.insert_coin(25)

        self.assertEqual(self.vending_machine.display(), "Current Amount: 25")

    def test_vending_machine_displays_insert_coin_when_no_coins_inserted(self):
        """should display 'INSERT COIN'"""
        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

    def test_product_is_dispensed_if_enough_money_is_received(self):
        """should dispense product if sufficient funds have been received"""
        for i in range(4):
            self.vending_machine.insert_coin(25)

        self.assertEqual(self.vending_machine.select_product("cola"), "cola")
        self.assertEqual(self.vending_machine.display(), "THANK YOU")

        self.assertEqual(self.vending_machine.display(), "INSERT COINS")
        self.assertEqual(self.vending_machine.current_amount(), 0)

    def test_machine_displays_price_if_insufficient_funds(self):
        """should display price of item if not enough funds have been received"""
        self.vending_machine.select_product("cola")

        self.assertEqual(self.vending_machine.display(), "PRICE: 100")
        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

    def test_product_is_dispensed_and_money_is_returned_if_money_left_over(self):
        """should dispense products and give back any extra money"""
        for i in range(4):
            self.vending_machine.insert_coin(25)

        self.assertEqual(self.vending_machine.select_product("chips"), "chips")

        self.assertEqual(self.vending_machine.return_coins(), [Coin(5.670, 24.26, 1.75, 25), Coin(5.670, 24.26, 1.75, 25)])

    def test_refund_coins(self):
        """should return all coins"""
        self.vending_machine.insert_coin(25)
        self.assertEqual(self.vending_machine.return_coins(), [Coin(5.670, 24.26, 1.75, 25)])

        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

    def test_machine_displays_sold_out_if_item_is_out_of_stock(self):
        """should display sold out if item is out of stock. Will display money left over"""

        for i in range(8):
            self.vending_machine.insert_coin(25)

        for i in range(2):
            self.vending_machine.select_product("cola")

        self.assertEqual(self.vending_machine.display(), "SOLD OUT")
        self.assertEqual(self.vending_machine.display(), "Current Amount: 100")

    # def test_machine_displays_exact_change_only_when_not_able_to_make_change(self):
    #     """vending machine displays exact change if not able to make change"""
    #     self.vending_machine.change['nickels'] = 1
    #
    #     for i in range(3):
    #         self.vending_machine.accept_coins(25)
    #
    #     self.vending_machine.select_product("candy")
    #
    #     self.assertEqual(self.vending_machine.display(), "EXACT CHANGE ONLY")
    #
    def test_machine_should_update_adding_of_coins(self):
        """update coin quantity"""
        self.vending_machine.insert_coin(25)

        self.assertEqual(self.vending_machine.change['quarters']['quantity'], 6)
    #
    # def test_machine_should_update_deleting_of_coins(self):
    #     """update coin quantity"""
    #
    #     for i in range(2):
    #         self.vending_machine.accept_coins(25)
    #         self.vending_machine.accept_coins(10)
    #
    #     self.vending_machine.accept_coins(5)
    #
    #     self.vending_machine.select_product("candy")
    #
    #     self.assertEqual(self.vending_machine.change['quarters']['quantity'], 7)
    #     self.assertEqual(self.vending_machine.change['dimes']['quantity'], 12)
    #     self.assertEqual(self.vending_machine.change['nickels']['quantity'], 11)
    #
    #     self.vending_machine.refund_coins()
    #     self.vending_machine.update_coin_inventory_when_refunding()
    #
    #     self.assertEqual(self.vending_machine.change['quarters']['quantity'], 7)
    #     self.assertEqual(self.vending_machine.change['dimes']['quantity'], 11)
    #     self.assertEqual(self.vending_machine.change['nickels']['quantity'], 11)


class TestCoinDetector(unittest.TestCase):
    """Tests for coin detector"""

    def setUp(self):
        self.coin_detector = CoinDetector([Coin(5.670, 24.26, 1.75, 25),
                                           Coin(2.268, 17.91, 1.35, 10),
                                           Coin(5.000, 21.21, 1.95, 5)])

    def test_coin_detector_should_identify_a_quarter(self):
        quarter = Coin(5.670, 24.26, 1.75)

        self.assertEqual(self.coin_detector.identify_coin(quarter), 25)

    def test_coin_detector_should_identify_a_dime(self):
        dime = Coin(2.268, 17.91, 1.35)

        self.assertEqual(self.coin_detector.identify_coin(dime), 10)

    def test_coin_detector_should_identify_a_nickel(self):
        nickel = Coin(5.000, 21.21, 1.95)

        self.assertEqual(self.coin_detector.identify_coin(nickel), 5)

    def test_returns_zero_for_invalid_coins(self):
        penny = Coin(2.500, 19.05, 1.52)

        self.assertEqual(self.coin_detector.identify_coin(penny), 0)


# class TestCoin(unittest.TestCase):
#
# test the eq

class TestCoinReturn(unittest.TestCase):
    def setUp(self):
        self.coin_return = CoinReturn([Coin(5.670, 24.26, 1.75, 25),
                                       Coin(2.268, 17.91, 1.35, 10),
                                       Coin(5.000, 21.21, 1.95, 5)])

    def test_return_value_of_100_returns_four_quarters(self):
        self.assertEqual(self.coin_return.return_coins(100), [Coin(5.670, 24.26, 1.75, 25), Coin(5.670, 24.26, 1.75, 25), Coin(5.670, 24.26, 1.75, 25), Coin(5.670, 24.26, 1.75, 25)])

    def test_return_value_of_sixty_five_returns_two_quarters_one_dime_one_nickel(self):
        self.assertEqual(self.coin_return.return_coins(65), [Coin(5.670, 24.26, 1.75, 25), Coin(5.670, 24.26, 1.75, 25), Coin(2.268, 17.91, 1.35, 10), Coin(5.000, 21.21, 1.95, 5)])

if __name__ == '__main__':
    unittest.main()
