from decimal import *

# create an array of coin values (list of coins in pence)
# note here we have changed the values from pence to pound by adding decimal
# All we've done is to divide each number by 100
coins = [1, .50, .20, .10, .05, .02, .01]


# define the give change function, it takes one param (the amount)
def give_change(amount):
    # create an empty list to hold our list of coins
    change = []
    # iterate through the list of coins
    for coin in coins:
        # to see if the coin is less than or equal to the amount
        if coin <= amount:
            # if it is we take off the value of the coin and add it to the list
            amount -= coin
            change.append(coin)
    return change


# challenge solution is below (give_change_decimal)
# its not being used as we were required to put it back to int from decimal
def give_change_decimal(amount):
    change_decimal = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change_decimal.append(float(coin))
    return change_decimal


'''
Line 25: We convert amount into a string, then a Decimal.
Line 27: We convert coin into a string, then a Decimal.
Line 29: Now when we do arithmetic, we are using Decimals so we avoid the floating point errors.
Line 30: We've to turn each coin back into a float, otherwise the list of coins would look like this:
[Decimal(0.1), Decimal(0.05), Decimal(0.02)], and the tests would fail
Replace your existing function with this one and try running the tests again
They should all pass this time
'''

'''
NOTE!!!!!!!!!!!!!
Our amount isn't actually 0, but a very small value approaching zero. Our bug is known as a floating point error,
or rounding error. It's outside the scope of this course to explain this fully, but essentially numbers such as 0.1
are known as floating point numbers, and are stored in such a way that doing arithmetic with them is error prone.
It's something to be aware of. You can see this by opening the Python console and doing 0.1 + 0.2:
'''
