###  

How to Load Test Data with Fixtures
===================================

##### In this unit the students will learn how to create JSON fixtures from their database using Django

 

### HOW TO LOAD TEST DATA WITH FIXTURES

Adding data to load into the test database is quite simple. First we’re going to
show you how to generate it.

The data we need is already existing in our development database, as we’ve been
creating it when we have manually tested our forum. So we simply need to dump
the data out:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ mkdir threads/fixtures
$ python manage.py dumpdata --indent 4 threads > 
threads/fixtures/subjects.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will generate a file filled with JSON, which defines our current set of
data:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[
{
    "fields": {
        "name": "General",
        "description": "<p><span style=\"font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;\">sdssdsfd</span></p>"
    },
    "model": "threads.subject",
    "pk": 1
},
{
    "fields": {
        "name": "Support",
        "description": "<p><span style=\"font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;\">dsdsd</span></p>"
    },
    "model": "threads.subject",
    "pk": 2
}
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This is our fixture or sample data that we will make the test system pull in
every time the tests are run.

The records here are then inserted so they can be used in our tests, so that our
call to Subject.objects.all() should return 2 objects.

To tell the test class to load that file, we add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HomePageTest(TestCase):
 
    fixtures = ['subjects']
 
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Because we added in the fixtures folder into the threads app folder, the test
will assume that the subjects.json file will be at
‘threads/fixtures/subjects.json’.

Unfortunately this won’t be enough because our functionality relies on user
data!

In order to get this to work we will need to run our **dumpdata** command again,
this time we’ll use the **accounts** app and we’ll store that in a
new **JSON** file called **user.json**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ python manage.py dumpdata --indent 4 accounts > threads/fixtures/user.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will create a JSON dump of our **accounts** app.

Now we’ll just have to make sure that we update our **HomePageTest** class to
load in the additional fixture.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HomePageTest(TestCase):
 
    fixtures = ['subjects', 'user']
 
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Once the class is instantiated in the testing process, the data will be loaded
into the relevant models and our queries will return valid testing data.

 

### ONE-OFF OBJECTS

Fixtures are very useful – but what if you only want one object for all your
tests? You could make a fixture that loads this in, but it can be simpler to
take advantage of another feature of the TestCase class – which is its ‘setUp’
method.

Each TestCase derived class also gets this method and can override it.

So in the case that we were testing our custom user authentication, we could
very well create one User that can be used to test our ‘loggedin’ view.

To make that one user available, we could attach it to
our **home.test** TestCase class instance like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from accounts.models import User
 
 
class HomePageTest(TestCase):
 
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='letmein')
        self.assertEqual(self.login, True)
 
    ...
 
    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user':self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

After we create the object, we can also make sure it’s logged in with our client
so that any checks on our ‘loggedin’ view would pass too.  

