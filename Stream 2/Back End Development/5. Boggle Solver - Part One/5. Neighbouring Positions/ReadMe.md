Neighbouring Positions
======================

 

### NEIGHBOURS

 

The grid and its letters are looking good. Let’s think about the `neighbours` of
a position. Time for another test:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_neighbours_of_a_position(self):
    neighbours = boggle.neighbours_of_position((1, 2))
    self.assertTrue((0, 1) in neighbours)
    self.assertTrue((0, 2) in neighbours)
    self.assertTrue((0, 3) in neighbours)
    self.assertTrue((1, 1) in neighbours)
    self.assertTrue((1, 3) in neighbours)
    self.assertTrue((2, 1) in neighbours)
    self.assertTrue((2, 2) in neighbours)
    self.assertTrue((2, 3) in neighbours)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Yet again we call a function that doesn’t exist yet. We call the function that
we wish existed. This helps us write code that does just enough. This test is a
good example of this.

 

A position on a grid will have `8` neighbours, unless it is on the edge or a
corner, in which case it will have less.

 

We are not concerned with those special cases yet. This function takes a
position and returns the `8` neighbours it should have. We’ll worry about
whether those neighbours are even in the grid elsewhere. We are separating the
two concerns.

 

It usually helps to start out writing dumb functions, and only make them smart
later if it makes sense. Dumb code tends to be simple code, and it’s much harder
to make complex code simple than it is to make simple code smart.

 

How can we make this test pass?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def neighbours_of_position((row, col)):
    return [ (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
             (row, col - 1),                     (row, col + 1),
             (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We explicitly specify the 8 neighbours of the **row** and **col**. See how the
code has been formatted to represent the relative positions of the neighbours?
This is an optional flourish, but it makes the purpose of the code instantly
apparent.

 

### NEIGHBOURS OF ALL POSITIONS

 

We’ve got a function that returns the potential neighbours of a position on the
board. But now we need to determine the actual neighbours for each position,
allowing for corners and edges.

 

Let’s write a test and see what that might look like:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_all_grid_neighbours(self):
    grid = boggle.make_grid(2, 2)
    neighbours = boggle.all_grid_neighbours(grid)
    self.assertEquals(len(neighbours), len(grid))
    for pos in grid:
        others = list(grid)  # creates a new list from the dictionary's keys
        others.remove(pos)
        self.assertListEqual(sorted(neighbours[pos]), sorted(others))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This is a much more complicated test than I would ordinarily be happy with. It’s
not immediately apparent what the test does, and loops and conditions in tests
are rarely a good thing. But we’ll leave it here as an example. See if you can
think of ways to simplify the test.

 

The trick to this test (and tricks are never good in tests) is that in a `2X2`
grid, every position touches every other position. So, the neighbours of any
position are the other three positions in the grid.

 

`Line 3` gets all of the neighbours for the grid. This is a dictionary where the
key is the position (just like with the grid itself), but the value is a list of
neighbouring positions).

 

This means that the `neighbours` dictionary will have 4 entries, each with a
list of 3 neighbours. So, `line 4` can assert the correct length of
the `neighbours` dictionary.

 

`Lines 5 to 8` iterate through the positions in the grid. For each position, the
neighbours are the other 3 positions on the grid. So, we create
the `others` list which is the full grid, minus the position in question.

 

It then asserts on **line 8** that these other positions are the neighbours of
the position being checked.

 

A complicated test, but it gives us confidence that our neighbours data
structure is correct.

 

Here’s how to implement the code that makes that test pass:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

For each position in the grid, get the possible neighbours using the function we
wrote earlier. Then the actual neighbours are those that are actually in the
grid. Simple.
