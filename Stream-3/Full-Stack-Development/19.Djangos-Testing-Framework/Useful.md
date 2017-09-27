Up until now, we’ve looked at writing features and testing by hand – but in this
section we’re going to look at Django’s support for automated testing of your
code.

Previously we’ve looked at the whole Django system right from models, views, and
urls. We’re now going to look into what strategies we can take to test each of
these aspects of our code, to make sure they are working as our site matures.

If at any point you run into any issues with your code, you can return to this
starting point by following these steps:

In the terminal run the following commands:

-   git clone <https://github.com/Code-Institute-Org/we_are_social.git>

-   cd we_are_social

-   git checkout angular_integration

Make sure you have a virtualenv setup in Pycharm. You’ll have to update the
requirements.txt file using `git+https://github.com/<your github id
here>/reusable_blog_app.git` instead of the link that’s already there. Once
that’s done, you can go ahead and install the dependencies from
‘requirements.txt.’

Run python manage.py migrate
