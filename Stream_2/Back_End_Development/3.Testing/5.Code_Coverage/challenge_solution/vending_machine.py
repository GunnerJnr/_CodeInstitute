from decimal import Decimal

# create an array of coin values (list of coins in pence)
# note here we have changed the values from pence to pound by adding decimal
# All we've done is to divide each number by 100
coins = [1, .50, .20, .10, .05, .02, .01]

# create a dictionary of available items in the vending machine with the cost of each
available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}


# define the give change function, it takes one param (the amount)
def give_change(amount):
    # create an empty list to hold our list of coins
    change = []
    amount = Decimal(str(amount))
    # iterate through the list of coins
    for coin in coins:
        coin = Decimal(str(coin))
        # while the coin is less than or equal to the amount
        while coin <= amount:
            # if it is we take off the value of the coin and add it to the list
            amount -= coin
            change.append(float(coin))
    return change


def give_item_and_change(item, amount):
    if item not in available_items:
        return None, amount, "that item isn't available"

    cost = available_items[item]

    if amount < cost:
        return None, amount, 'not enough money'

    change_to_return = float(amount) - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change"


if __name__ == '__main__':
    while True:
        item = raw_input('choose item: %s' % available_items)
        amount = raw_input('enter amount in pounds:')
        print give_item_and_change(item, amount)
