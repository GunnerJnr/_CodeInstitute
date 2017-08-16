# import the unit test module
import unittest
from vending_machine import give_change
from vending_machine import give_change_decimal


# define a class (inherits from unittest)
class TestVendingMachine(unittest.TestCase):
    # define our method (must because with test_ otherwise the test will not run)
    def test_return_change(self):
        # we're imaging there is a method called give_change which returns a list of coins
        # given in an amount in pence
        self.assertEqual(give_change(.17), [.10, .05, .02], 'wrong change given')
        self.assertEqual(give_change(18), [.10, .05, .02, .01], 'wrong change given')

        # decimal test
        self.assertEqual(give_change_decimal(.17), [.10, .05, .02], 'wrong change given')
        self.assertEqual(give_change_decimal(18), [.10, .05, .02, .01], 'wrong change given')

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(.04), [.02, .02])

        # decimal test
        self.assertEqual(give_change_decimal(.04), [.02, .02])
