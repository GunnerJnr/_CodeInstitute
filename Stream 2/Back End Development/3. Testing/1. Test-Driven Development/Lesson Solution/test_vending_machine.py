# import the unit test module
import unittest


# define a class (inherits from unittest)
class TestVendingMachine(unittest.TestCase):
    # define our method (must because with test_ otherwise the test will not run)
    def test_return_change(self):
        # we're imaging there is a method called give_change which returns a list of coins
        # given in an amount in pence
        coins = give_change(17)
        self.assertEqual(coins, [10, 5, 2], 'wrong change given')
