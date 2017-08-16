CHALLENGE
=========

 

Try using the decimal module (<https://docs.python.org/2/library/decimal.html>)
to deal with the floating point issues and make the tests pass. It can be used
like this:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> from decimal import *
>>> Decimal('0.1') + Decimal('0.2')
Decimal('0.3')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 

NOTE:

You’ll have to convert the Decimal back to a float, otherwise the test will be
comparing Decimals to ints. In the same way that int is shorthand for Integer,
float is shorthand for Floating Point number.

 

The answer is shown in the `give_change_decimal` method, this is where we finish
making the vending machine.

 

 
