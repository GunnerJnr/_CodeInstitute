###  

### HOW TO TEST VIEWS AND URLS

The basic things you want to test with views and urls are:

1.  That a url resolves to the correct view function

2.  That your view shows the right information

 

### URLS

So let’s look at checking the url resolving with a basic home page check. Add
this code to the **test.py** file in your **home** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
 
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So here we create a test case based on our TestCase class that enables a testing
web server. We then use Django’s resolve function to feed in the URL for the
home page.

This gives us the internal representation of the home page and also a handle to
the function that would be used to process the request in
the `home_page.func` member variable.

All we need to do here is make sure that when we call that function, it matches
the view function we have declared in our views.py.

If it doesnt match, then there’s something wrong with our urls.py file that
needs fixing!

 

### VIEWS

Testing views is a little more complex, as we may want to check a few more
things than just the resolve of a url.

Things that we could check are:

-   Does it return the correct status code?

-   Does it return the right content?

-   Does it use the correct template?

-   Does it show the correct success/fail messages?

So let’s check some content on our first page of our forum:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_home_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEqual(home_page.status_code, 200)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This is our first chance to use the `self.client`, which is used to visit the
url in our test webserver and grab the content and HTTP headers, etc.

As you would expect, you get a Python object back containing all the information
relating to what happened when it visited the URL.

Our first task is to check the status_code, so that we can be certain that the
page returns the actual page and not a 404 or 500 error page.

Next we can do our checks on the content and the template that was used:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render_to_response
...
    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

By passing in the `home_page` response object and the name of the template,
our `assertTemplateUsed()` function can check in the response if the template we
expect to be used is the one that’s actually used. This is important as this
protects us from accidentally changing templates in our code and then trying to
commit them into our main production code.

If we didn’t know that this had changed, then the alternative template might
find its way onto our live site!

Finally, we check that the output of the template from the URL is the same as
what we expect when we use `render_to_response` to directly render its output
locally. This ensures that there are no extra stages affecting our page
rendering without us knowing about it.

 

### NOTE

Like the ‘render’ function you use in your view
functions, `render_to_response` can take arguments to render other pages like
the forums subjects or threads.

 

So when you’re rendering this view, we need to supply this test with some
subjects like the real view would have – or else our template would fail to
render.

In **threads/tests.py** add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject
 
 
class SubjectPageTest(TestCase):
 
    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

That way our template will render just like it would in our view and we have
reproduced the correct list of items.However, that leads to an interesting
question. Where does the list of Subjects come from?

As we said earlier, the tests have a testing database that’s empty every time
you start the tests – so we will need to add in some data to do this.
