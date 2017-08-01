The Efficiency of Algorithms
============================

 

In the last module we limited the size of the grid to 3×3, and even that took
some time to complete. If you increase the size to 4×4, you will be waiting a
long time for results. Try it – but feel free to hit stop after 20 minutes.

 

The problem is not your machine. A more powerful machine will perform a like for
like task more quickly, but some algorithms have issues that can not be overcome
with more power.

 

Notice that a relatively small increase in board size let to a massive increase
in processing time to complete the task. You can imaging that further increases
to 5×5 or 10×10 would push the algorithm beyond the capabilities of even very
powerful machines. Grids of 100×100 or larger would simply be out of the
question entirely.

 

We don’t need such large grids for Boggle, but there are problems that require
those kinds of search spaces, and we need to be able to deal with them.

 

In this module we’ll see that we can achieve gains with relatively small changes
to our algorithm that could not be achieved by even the most powerful and costly
upgrades to our hardware.

 

We’ll start by pinpointing exactly where we lose most time and improve the
efficiency of that code. After that we’ll look at our algorithm and see if we
can reduce the search space to reduce the exponential growth in search space
that results from larger board sizes.

 

### EXPONENTIAL GROWTH

 

The amount of word combinations is said to have **factorial growth** as the grid
size increases. This means that a grid with 4 letters has
roughly **4!** combinations.

4! means 4 factorial = 4 \* 3 \* 2 \* 1.

 

In contrast, the number of letters has quadratic growth compared to the width
and height of the grid. A 2×2 grid has 4 letters, 3×3 has 9, etc.

 

We can use factorial in the Python shell by importing it from the math module:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from math import factorial
>>> factorial(4)
24
>>> factorial(9)
362880
>>> factorial(16)
20922789888000L
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

For a 4×4 grid, there are roughly 20 trillion combinations. It’s such a large
number that Python has had to automatically convert it to a long number, hence
the L at the end.

  
This is why the run time for a search of a 4×4 grid is so much longer than for a
3×3.

 

### NOTE:

There is a saying that goes:

`‘Premature optimization is the root of all evil’, which means don’t try and
optimise programs if they don’t need it. More specifically, don’t try to
optimise programs before you know where and why they are slow. Many developers
have gone down the rabbit hole of micro optimisations that really don’t matter
in the grand scheme of things.`

 

In our case, we have to find a way to improve this algorithm. A normal Boggle
grid is 4 x 4 and our program is simply too slow to run it.
