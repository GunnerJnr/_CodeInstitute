CHALLENGE A
===========

Create a new directory to the templates folder and create a template called
magazines.html, a URL and a view that will load all the Magazines and show them
using the Django template language and a link to the new magazine page to the
base.html file.

 

CHALLENGE B
===========

Because our magazine’s template tag required an instance of the user object, the
page will throw an error if you’re not logged in. Try adding a `login_required`
decorator to the magazine view that you created in the previous challenge that
will redirect someone to the /login/ URL if they’re not logged in.
