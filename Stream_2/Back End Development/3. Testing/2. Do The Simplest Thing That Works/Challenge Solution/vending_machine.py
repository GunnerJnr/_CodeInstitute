# create an array of coin values (list of coins in pence)
coins = [100, 50, 20, 10, 5, 2, 1]


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
