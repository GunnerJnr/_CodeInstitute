### UNIT TESTING OUR MODEL

Before we go any further, it would be a good idea to check whether
our **Post** class does what we intended it to do. We could create an instance
of the Post class in our Python shell and try to create new post entries like we
did in an earlier lesson –  but once the shell is closed, that test code is
gone.

Wouldn’t it be handy if we could create some code just once that we could
repeatedly run when testing a project and its functionality? Django provides
just the thing for that.

Remember, good programming is lazy, or DRY, programming. A unit test does what
the name implies; it is a test of a small unit of work, and in our case, a unit
of work is the instantiation of the **Post** class and its functions.  
  
**To quote the Python Wiki:**

 *Here are some observations about debugging:*

-   *Practically all software has some bugs; it’s a matter of frequency and
    severity rather than absolute perfection.*

-   *The sooner you find a bug, the better: amongst other things, that it avoids
    wasting other people’s time when they’re bitten, and it makes schedules less
    likely to slip through extended debugging.*

-   *When a bug does occur, you want to spend the minimum amount of time getting
    from the observed symptom to the root cause.*

Django provides a file called **tests.py** out of the box in our apps for
writing unit tests. The test mechanism itself is built up on Python’s core
testing functionality.

So, how do we unit test? We create a test class for each model or function in
our app inside tests.py. If we are testing a model or function that accesses a
database, then that class must inherit from **django.test.TestCase** –
otherwise, it must inherit from the python core **unittest.TestCase** class.

Create a new class inside **tests.py** called **PostTest**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from .models import Post
 
 
class PostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """
 
    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                          'My Latest Blog Post')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s new in this code?**

Look at the imports; the first line contains a Django-specific test import. The
second line contains a dot (**.**) prior to the model name. This tells Django
that the models file is in the same directory as **tests.py**. This is useful to
avoid any confusion in larger projects with multiple apps
containing **models.py** files.

We’ll use this approach from now on.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from .models import Post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We defined a function called **test_str** that the instance of
the **PostTest** class as a parameter.it. We then create an instance of the Post
class and initialize the title with some text and save the instance to
the **test_title** variable.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we use a special test function called **assertEqual**. You’ll remember from
Stream 2 that assertEqual is essentially a function that checks that two
variables are equal to each other. In our case, we check if the title written to
the database equals the expected title.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.assertEqual(str(test_title),
                          'My Latest Blog Post')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once we run the test, **assertEqual** will either return “OK” if the test
passes, or will return false if it does not. In this case, it will try to show
where the discrepancy is located. Run the following command in your command line
interface (or terminal interface within Pycharm). The command will run all tests
within our blog app’s **test.py**.

python manage.py test blog

If your test passes, you should see OK printed out to the screen.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449505716_image1.png)

  
Change the asserted title text so that it differs from the created title (e.g.
change the text from say “blog” to “bloggy”), and you’ll get a failure message.
See how Python helps us by trying to identify the differences in the expected
post title and the actual title added to the database.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449505716_image2.png)

  
Notice also that, in both cases, a temporary copy of our database is created for
our test, then destroyed once the test has finished running. This is a great
approach because it protects any “good” data that might be already in the
database from being mistakenly corrupted by testing, and also prevents us from
littering the database with test data.
