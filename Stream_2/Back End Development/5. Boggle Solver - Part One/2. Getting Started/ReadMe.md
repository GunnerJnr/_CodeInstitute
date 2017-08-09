Getting Started
===============

 

### GETTING STARTED

The following is our unit test ritual that we will follow every time we start a
new project. It won’t always be described in this level of detail in the notes,
but you should get into the habit of starting projects with a test, so that it
becomes natural for you.

 

Create a new Python project. Create two files, `boggle.py` and `test_boggle.py`.

Add the following initial test to `test_boggle.py` (we’ll delete this later):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
import boggle
 
class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_On(self):
        self.assertEquals(1, boggle.check())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

If you run this test, it will fail because
the [function](http://codeinstitute.wpengine.com/glossary/function/) check
doesn’t exist in `boggle.py`. Create
the [function](http://codeinstitute.wpengine.com/glossary/function/) in `boggle.py`,
but have it return `0` instead of `1`, so that the test still fails.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check():
    return 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Running the test shows an assertion error, as expected.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AssertionError: 1 != 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now, modify
the `boggle.check` [function](http://codeinstitute.wpengine.com/glossary/function/) to
return `1` instead of `0` and the test should pass. You’ve successfully hooked
up your code file `boggle.py` to your unit tests in `test_boggle.py`.

 

Now we can start writing the real unit tests and the code that will make them
pass.
