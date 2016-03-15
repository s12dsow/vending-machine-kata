import unittest
from vending_machine.vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    """Tests for vending machine"""
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_vending_machine_accepts_quarters(self):
        """should accept valid coins"""
        self.vending_machine.accept_coins(25)

        self.assertEqual(self.vending_machine.current_amount(), 25)

    def test_vending_machine_accepts_dimes(self):
        """should accept valid coins"""
        self.vending_machine.accept_coins(10)

        self.assertEqual(self.vending_machine.current_amount(), 10)

    def test_vending_machine_accepts_nickels(self):
        """should accept valid coins"""
        self.vending_machine.accept_coins(5)

        self.assertEqual(self.vending_machine.current_amount(), 5)

    def test_vending_machine_rejects_pennies_and_returns_them(self):
        """should reject and put pennies in coin return"""
        self.vending_machine.accept_coins(1)

        self.assertEqual(self.vending_machine.return_coins(), 1)

    def test_vending_machine_updates_display_when_valid_coin_accepted(self):
        """should update display when received valid coin"""
        self.vending_machine.accept_coins(25)

        self.assertEqual(self.vending_machine.display(), "Current Amount: %d" % self.vending_machine.current_amount())

    def test_vending_machine_displays_insert_coin_when_no_coins_inserted(self):
        """should display 'INSERT COIN'"""
        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

    def test_vending_machine_has_stock(self):
        self.assertEqual(self.vending_machine.products, {"cola": 100, "chips": 50, "candy": 65})

    def test_product_is_dispensed_if_enough_money_is_received(self):
        """should dispense product if sufficient funds have been received"""

        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)

        self.assertEqual(self.vending_machine.select_product("cola"), "cola")
        self.assertEqual(self.vending_machine.display(), "THANK YOU")

        self.assertEqual(self.vending_machine.display(), "INSERT COINS")
        self.assertEqual(self.vending_machine.current_amount(), 0)

    def test_machine_displays_price_if_unsufficient_funds(self):
        """should display price of item if not enough funds have been received"""
        self.vending_machine.select_product("cola")

        self.assertEqual(self.vending_machine.display(), "PRICE: 100")
        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

    def test_product_is_dispensed_and_money_is_returned_if_money_left_over(self):
        """should dispense products and give back any extra money"""
        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)
        self.vending_machine.accept_coins(25)

        self.assertEqual(self.vending_machine.select_product("chips"), "chips")
        self.assertEqual(self.vending_machine.return_coins(), 50)

    def test_return_coins(self):
        """should return all coins"""
        self.vending_machine.accept_coins(25)
        self.vending_machine.refund_coins()

        self.assertEqual(self.vending_machine.return_coins(), 25)
        self.assertEqual(self.vending_machine.display(), "INSERT COINS")

if __name__ == '__main__':
    unittest.main()
