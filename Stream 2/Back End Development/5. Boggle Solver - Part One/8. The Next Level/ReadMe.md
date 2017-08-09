The Next Level
==============

 

The notes in the previous lesson mention that the algorithm as it stands has
some performance issues and we’ve limited the size of the grid to `3×3`. In the
next module we’ll look at why that is, and what we can do about it.

### SUMMARY

 

In this lesson, you’ve:

-   Incrementally built up an algorithm to solve Boggle.

-   Used tests to drive the design towards smaller self contained functions.

-   Used various data structures to model the boggle grid and dictionary.

-   Used recursion to solve a problem which couldn’t be solved as easily with
    for-loops.

 

**COMPLETED CODE**  
The code for the previous lessons can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit05-Boggle_pt_1>

 

CHALLENGE
=========

 

-   Change the program so that it works with a `2×2` grid, and then again with a
    `3×3` grid. Use a stopwatch to get an approximate idea of the difference in
    time taken to run. Now, estimate (or just take a wild guess) how long you
    think a `4×4` grid would take. In the next module, we’ll see if you’re
    right.

 

-   Go back and read the tests again in order, and try to recall how you made
    each one pass, then look at the code and see how much of the program you
    actually remember. Use a notebook to write down the parts you had forgotten.

 

-   Refactor the
    main [function](http://codeinstitute.wpengine.com/glossary/function/) to
    extract the code for displaying the words and put it in a method
    called `display_words`.

 

HINT
====

 

The code we’re currently using to display the words is the last three lines of
the `main()` method. Remove them from there and move them into a new method
called `display_words`. This method should take in the words returned from the
search method.

 

SOLUTION
========

 

In case of emergency, break the glass! Find the solution to this challenge
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit05-Boggle_pt_1/challenge>

 

Please Note:

 

This is the solution of the code institute, my actual solution will follow in
the near future, due to work and time restrictions I will be rushing through the
course to get the content complete and coming back to the solutions at a later
date. Thanks
