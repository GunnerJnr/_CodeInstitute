Bringing It All Together
========================

 

Our Boggle program is just a list of functions. If you run it, nothing happens.
This is because there is not code to actually execute the functions. Until now
we have only executed the code by running tests.

 

Thankfully, because we used tests to drive out the development of the code, we
already have all the building blocks for our boggle solver. We just need to get
them to work together.

 

No test this time (we could write another one, but we’re not trying to be
perfect here). Let’s just write a function that will generate a random board,
load a dictionary, find the words, and print them out. Place this function at
the bottom of the `boggle.py` file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    grid = make_grid(3, 3)
    dictionary = get_dictionary('/usr/share/dict/words')
    words = search(grid, dictionary)
    for word in words:
        print word
    print "Found {0} words".format(len(words))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Note we made the grid `3×3`. Even at this reduced size, the program will take
some time to run. Our functionality is all ok, but our performance is poor.
We’ll deal with this in the next module.

 

If you read the paragraph above that described what we want the program to do,
then read the code – they’re a pretty close match. If we moved the code for
printing the words out into their own function, then our code would read like a
high level description of what the program does, with no details about how it’s
done.

 

That higher level of abstraction, which makes code read like prose, is what you
should be aiming for. And composing programs from smaller pieces, as we’ve done
here, is the best way to achieve it.

 

However, our program still won’t run. All we’ve done is create yet another
function. We need to add one more line of code at the bottom of the file, to
call `main()`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now when we run `boggle.py`, it will (eventually) give us the results.

![](img/bringingitalltogether.png)
