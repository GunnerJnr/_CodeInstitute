Defining The Grid
=================

 

We need a way to store the letters in our grid. Each grid position should hold a
random letter from the alphabet. We could use the same method we used in the
last unit for storing our position in the map; a dictionary. But, we’re getting
too far ahead of ourselves.

 

### AN EMPTY GRID

Let’s write a unit test.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_can_create_an_empty_grid(self):
    grid = boggle.make_grid(0, 0)
    self.assertEquals(len(grid), 0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Notice that
this [function](http://codeinstitute.wpengine.com/glossary/function/) doesn’t
make any assumptions about the data structure used to implement our grid. It’s
simply a test that suggests the need for a way of making a grid of letters.

 

We have options here – we could assume that boggle grids are always square, in
which case we only need pass a size to `make_grid`. We could assume that they
are always `4×4`, in which case we don’t need to pass any size arguments at all.

 

We opt for the most flexible option – we can pass two arguments, `height` and
`width`, or rows and columns if you prefer.

 

We use the simplest possible grid – one with no `rows` or `columns` for our
first test.

 

Of course this test fails, because `make_grid` hasn’t been implemented yet, so
get the test passing by adding
that [function](http://codeinstitute.wpengine.com/glossary/function/) to `boggle.py`.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_grid(width, height):
    return {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

That’s a simple solution that makes the test pass. We’re only concerned with an
empty grid at this point.  


### A GRID WITH POSITIONS

Let’s make it so that our grid can actually have positions. Here’s a test:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_grid_size_is_width_times_height(self):
    grid = boggle.make_grid(2, 3)
    self.assertEquals(len(grid), 6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This test simply asserts that when we do give the grid some dimensions, we
actually get the right number of positions.

 

Here’s a solution that creates a dictionary with a `row`, `column` tuple as the
key, and a space as the value. We’re not concerned with the letters yet.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def make_grid(height, width):
    return {(row, col): ' ' for row in range(height)
                            for col in range(width)}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now we have a possible data structure. We could have taken smaller steps here to
make the test pass, but we’ll move on.  


### COORDINATES

Now that we can create grids, we can check if a given position `(row, col)` is
in the grid.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_grid_coordinates(self):
    grid = boggle.make_grid(2, 2)
    self.assertTrue((0,0) in grid)
    self.assertTrue((0,1) in grid)
    self.assertTrue((1,0) in grid)
    self.assertTrue((1,1) in grid)
    self.assertTrue((2,2) not in grid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We’re still not interested in the letters in the grid, but already we’re getting
a feel for how we might work with our grid data structure.

 

That test will actually pass already. No need for any code changes.
