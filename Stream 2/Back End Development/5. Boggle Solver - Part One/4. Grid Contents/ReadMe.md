Grid Contents
=============

 

### FILLED WITH LETTERS

 

It’s time to make sure that our grid is filled with letters. Here’s a test:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_grid_is_filled_with_letters(self):
    grid = boggle.make_grid(2, 3)
    for L in grid.values():
        self.assertTrue(L in ascii_uppercase)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The `ascii_uppercase` mentioned on `line 4` is simply a list of the `26 UPPER
CASE ascii characters (A-Z)`. It must be imported. Add the following at the top
of your `test_boggle.py` file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from string import ascii_uppercase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The test creates a grid and then asserts that every value in the grid is an
upper case letter. At the moment they are not because we filled the grid with
spaces. So the test will fail. So, let’s make it pass.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
                for row in range(height)
                for col in range(width)}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We amend
the `make_grid` [function](http://codeinstitute.wpengine.com/glossary/function/) to
return a choice of `ascii_uppercase` character, rather than a space. In
practice, what does that mean?

 

We need to import `ascii_uppercase` in our `boggle_py`, just as we did
in `test_boggle.py`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from string import ascii_uppercase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The `choice` [function](http://codeinstitute.wpengine.com/glossary/function/) returns
an item from a list at random. We need to import it to** **`boggle.py` too.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from random import choice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
