No Challenge
============

 

This lesson didn’t contain a challenge.

 

We did however install the Pycharm IDE and create a new program called ‘guess
the number’. It comprised of the following python code file:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import the library for generating random numbers
import random

# create and assign our constant variables
NUM_OF_GUESSES = 10
RANGE = 10

# create an infinite loop so the game can run indefinitely
while True:
    # generate the random number between 0 and range (10)
    rand_num = random.randint(0, RANGE)

    # give the user a certain amount of guesses (10)
    for i in range(NUM_OF_GUESSES):
        # store the user input (guess)
        guess = raw_input('guess the number: ')
        # compare the numbers
        if guess == rand_num:
            # if equal print message and exit the loop
            print 'well done'
            break
        # otherwise state whether the users guess was too high or too low
        elif guess > rand_num:
            print "too high"
        else:
            print "too low"
    # we print this once the user has used all their guesses
    # or has correctly guessed the number (restart the game)
    print "let's try a new number!"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

NOTE!!!!
========

>   Play the game a few times. Eventually **you’ll notice that something is
>   going wrong:** it always says too high and the number is impossible to
>   guess. Unlike a syntax error, there is no error message telling us where the
>   problem is, so we’ll have to try and work out what’s happening by using the
>   debugger.

 
