# import the library for generating random numbers
import random

# create and assign our constant variables
bGameOver = True
NUM_GUESSES = 10
MAX_RANGE = 10

# create an infinite loop so the game can run indefinitely
while bGameOver:
    # generate the random number between 0 and range (10)
    rand_num = random.randint(0, MAX_RANGE)

    print "Try to guess the number between 0 and " + str(MAX_RANGE)
    print "You have " + str(NUM_GUESSES) + " guesses"

    # give the user a certain amount of guesses (10)
    for i in range(NUM_GUESSES):
        # store the user input (guess)
        # NOTE we removed the bug here by converting the users input (a string) to an int
        # the program now works as expected
        guess = int(raw_input('guess the number: '))
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

        NUM_GUESSES -= 1
        if NUM_GUESSES >= 1:
            print "You have " + str(NUM_GUESSES) + " guesses left"

        if NUM_GUESSES == 0:
            print "Sorry, You Lose!"
            bGameOver = False
            break

    bGameOver = True
    NUM_GUESSES = 10
    # we print this once the user has used all their guesses
    # or has correctly guessed the number (restart the game)
    print "Let's try a new number!"
