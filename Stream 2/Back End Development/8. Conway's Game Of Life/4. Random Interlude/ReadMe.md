Random Interlude
================

 

`Random numbers generators (RNGs)` are quite interesting, and it’s worth reading
about them, e.g.<https://en.wikipedia.org/wiki/Random_number_generation>.

 

There are two types of RNGs:

-   `True:` Generates numbers based on an actual random physical source, for
    instance quantum phenomena.

-   `Pseudo:` Generates long sequences of numbers which look random but are
    actually based on an algorithm.

 

It often comes as a surprise that most RNGs aren’t actually random, but you can
see this by setting a seed:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> random.seed(0)
>>> [random.randint(0,10) for i in range(10)]
[9, 8, 4, 2, 5, 4, 8, 3, 5, 6]
>>> random.seed(0)
>>> [random.randint(0,10) for i in range(10)]
[9, 8, 4, 2, 5, 4, 8, 3, 5, 6]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can see in **lines 3** and **6** that the same sequence of random numbers has
been returned. True randomness is very important for cryptographic applications,
as you can see by the warning in the documentation for the random module:

 

![](img/1.png)

 

See <https://en.wikipedia.org/wiki/Random_number_generator_attack> for more
information.
