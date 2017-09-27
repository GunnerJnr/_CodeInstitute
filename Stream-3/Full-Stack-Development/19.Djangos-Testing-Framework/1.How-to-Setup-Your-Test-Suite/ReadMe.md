How to Setup Your Test Suite
============================

##### In this unit the students will learn how to set up a test suite in Django

 

### HOW TO SETUP YOUR TEST SUITE

First things first – let’s get setup with the testing framework and get familiar
with how Django provides testing.

Each app that you create within your project will need a *tests.py* file added
to it, which will contain our testing code. This is normally created for you on
your apps, but it won’t be there for your main project folder if you need to run
tests on that part of your site – but you can simply create one by hand.

Now that’s installed, we can begin creating tests for our features! But what
kind of tests does Django support?  


### WHAT TESTING OPTIONS ARE AVAILABLE

Testing in Django takes the form of creating a class in our *tests.py* file and
deriving it from one of a selection of existing classes that Django provides to
support your different types of tests.

To create a test, you create your class derived from one of the classes and then
create a class method that is named starting with with `test_`, like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from unittest import TestCase
 
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1 + 2, 3 )
 
    def test_adding_something_isnt_equal(self):
        self.assertNotEqual( 1 + 2, 4 )
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Here we have two different class methods we’ve added to the most
basic `TestCase` class that Django provides. In each case, we name the function
starting with `test_`, then give it a unique name that describes what it does.

 

### NOTE

We also did two checks to make sure that adding works correctly. One to check
that it gives the right result and another to check that it also doesn’t give a
wrong result. This is often a good starting point when your looking for ideas of
where to begin testing your code.

 

### RUNNING OUR TESTS

Now we have a simple test we can run and see what sort of report we will get
back from Django. From the command line, we can run the tests like so:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
python manage.py test <app name>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

If you had put the test code into the ‘accounts’ app from our forum unit, you
might expect to see the following output:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ python manage.py test accounts
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s
 
OK
Destroying test database for alias 'default'...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

`python manage.py` tasks can be run directly from with PyCharm using the *Run
manage.py task*option from the Tools menu.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/lesson26image1.png)

You can run the ‘test’ task to run all tests, or include an app name to run the
tests in a specific app.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/lesson26image2.png)

PyCharm displays the results:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/lesson26image3.png)

So that’s what a successful test looks like, but what should a failed test look
like?

Let’s change our last test so that instead of returning the incorrect result, it
actually returns correct – which is not what we want:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from unittest import TestCase
 
class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1 + 2, 3 )
 
    def test_adding_something_isnt_equal(self):
        self.assertNotEqual( 1 + 2, 3 ) # changed to make the assertNotEqual test fail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we re-run the tests, we should now see the last test fail:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/lesson26image4.png)

And as you can see, we have a Traceback that shows us the line number, the code
that failed, and the reason why it failed. We also see that whilst two tests
where run, there was only one failure – so we can see it wasn’t all of our tests
that went wrong.

In this way we can write tests that describe how some code should behave, then
write code in our features that pass these tests. This is a technique
called **test driven design** or **TDD**.

The idea is that before you write any actual features, you write the tests that
the code should be able to pass, then write your feature code so that it will
pass the test. Every time you write some code that changes a feature, you run
the tests and it will tell you if your code is meeting the requirements or not.  


### AVAILABLE TEST CLASSES

Let’s take a moment to look over what’s available in the framework for testing
classes so we can understand what they are and what they are for.

Firstly we have the `unittest.TestCase` class, the most basic test class. It
provides these assert functions we’ve just used to check if the values were
equal or not equal, in addition to a few others.

After providing that basic class, Django then provides some more advanced
classes:

-   `django.test.SimpleTestCase` – Provides assert functions for checking form
    field validation, HTML assert functions, and also loads in your Django
    settings.py.

-   `django.test.TestCase` – Loads in fixtures into a the testing database
    before running tests. Creates a ‘Test Client’ called `self.client`, which
    can be used to fetch web pages and resolve urls. Adds in various additional
    Django specific asserts.

-   `django.test.TransactionTestCase` – Loads in fixtures into the testing
    database before running tests. Creates a ‘Test Client’ called self.client
    which can be used to fetch web pages and resolve urls. Adds in various
    additional Django specific asserts. Additionally allows for testing database
    transactions and automatically resets your database at the end of the test
    run.

-   `django.test.LiveServerTest` – Does the same thing as TransactionTestCase,
    but also starts a proper webserver when performing testing instead of the
    ‘Test Client’.

So now that you know what’s available – which one should you choose?

The idea is to pick only the one that provides the most basic set of testing
features you will use. Each test class requires more and more, so the testing
will take longer. Choose the one that loads in the least, so your testing time
will only be as long as it needs to be!

Now we are going to look at testing the various parts of our apps, starting with
the most basic part of Django – views and urls.
