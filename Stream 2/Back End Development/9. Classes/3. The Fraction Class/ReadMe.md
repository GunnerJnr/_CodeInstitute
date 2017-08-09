THE FRACTIONS CLASS
===================

 

Classes can also be made to work with Python’s built in operators
such **+**,**–**,**\***,**/**,**,and \> by adding dunder methods.
The Fraction class allows the user to define a fraction:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We’re defining a fraction using the top and bottom numbers separately, otherwise
known as the numerator and denominator.

 

The problem with this class is that it doesn’t output a very useful
representation when printed:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f = Fraction(1,2)
>>> f
<__builtin__.Fraction instance at 0x025327D8>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can remedy this by giving it **a \_\_repr\_\_ method**, short for
representation:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def __repr__(self):
    return '%s/%s' % (self.num, self.den)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The value returned from
the [function](http://codeinstitute.wpengine.com/glossary/function/) is the
value that will be printed.

 

The **\_\_str\_\_ method** can also be used for this purpose but
using **\_\_repr\_\_** will also make sure it’s printed correctly when using the
Python console:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f = Fraction(1,2)
>>> f
1/2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

It’d be useful if we could add fractions together. Let’s give it a go:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f1 = Fraction(1,2)
>>> f2 = Fraction(1,4)
>>> f3 = f1 + f2
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'instance' and 'instance'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Python doesn’t know how to add our classes together because we haven’t told it
yet. We can do this by using the **\_\_add\_\_** dunder method:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def __add__(self, other):
    num = self.num * other.den + self.den * other.num
    den = self.den * other.den
    return Fraction(num, den)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The first argument to **\_\_add\_\_** (after self) is the instance of the other
fraction we will be adding to. Using the standard technique to sum fractions, we
create a new Fraction and return it. Rerun the new code in the console, and try
adding the fractions again. You should see it has printed out the correct
result:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f1 = Fraction(1,2)
>>> f2 = Fraction(1,4)
>>> f3 = f1 + f2
6/8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can now add the subtract, multiply and divide methods:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def __sub__(self, other):
    num = self.num * other.den - self.den * other.num
    den = self.den * other.den
    return Fraction(num, den)
 
def __mul__(self, other):
    return Fraction(self.num * other.num, self.den * other.den)
 
def __div__(self, other):
    return Fraction(self.num * other.den, self.den * other.num)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

There are many other dunder methods which can be implemented, some of which are
more applicable than others. For
instance, **\_\_eq\_\_**, **\_\_ne\_\_**, **\_\_lt\_\_**, **\_\_gt\_\_**, **\_\_le\_\_**,
and **\_\_ge\_\_** correspond to the comparison
operators **=**, **!=**, **, \>, , and \>=, which would be useful for this
class. On the other hand, \_\_contains\_\_ would let us override the in keyword
and let us evaluate fraction1 in fraction2, but it doesn’t make a lot of sense
and is ambiguous.**

 

You can read more about Python’s magic methods
here: <https://docs.python.org/2/reference/datamodel.html#special-method-names>

 

Python actually has a Fraction class built in – you can import it by using from
fractions import Fraction. You can use it to test the correctness of your
program when trying some of the challenges below.

 

### SUMMARY

In this lesson you have:

-   Learned about classes, and used inheritance to specialise a class while
    making use of existing methods in the parent

-   Used private class members to hide details of the class from the rest of the
    program

-   Created a class to model fractions and enabled it to work with common
    arithmetic operators

 

CHALLENGE
=========

-   Implement the magic methods necessary to allow comparisons such
    as **=**, **!=**, **, and \> between two fractions**

 

-   It would be better if our Fraction class converted fractions down to their
    lowest common denominator, so that 4/2 became 2/1. This can be achieved by
    finding the greatest common denominator (GCD) between the numerator and
    denominator. Use
    the **gcd** [function](http://codeinstitute.wpengine.com/glossary/function/) in
    the fractions module to do this in the initialiser.

 

-   **Difficult**: modify** \_\_repr\_\_** so that vulgar fractions are
    displayed properly, e.g. 2 ¼ instead of 9/4. You can use the built in
    divmod [function](http://codeinstitute.wpengine.com/glossary/function/) to
    get quotient and remainder.

 

-   **Very difficult**: modify the initialiser to accept floating point numbers
    such as 0.2 and create a fraction out of them. You could try multiplying the
    number by an increasing value until it becomes an integer, e.g. 0.2 \* 5 = 1
    so you know that it equals ⅕. Watch out for floating point issues though!

 

Please Note:

My actual solution will follow in the near future, due to work and time
restrictions I will be rushing through the course to get the content complete
and coming back to the solutions at a later date. Thanks
