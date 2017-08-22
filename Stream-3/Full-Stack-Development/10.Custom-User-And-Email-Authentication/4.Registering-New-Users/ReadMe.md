### REGISTERING NEW USERS

Now that we’ve laid down the basics to allow our user to authenticate with their
email address, we need to take care of the process of actually creating new
users.

The method we’ve chosen is to collect the user’s information and automatically
log them in, as this is a common practice these days and is considered to be a
best practice in assisting the user to access your sites, without slowing them
down or discouraging them.  


### CREATE THE FORMS

In the accounts app create a file called ‘forms.py’ and add the following code
to create the UserRegistrationForm:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError 
 
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
 
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
 
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)
 
        return password2
 
    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
 
        # automatically set to email address to create a unique identifier
        instance.username = instance.email
 
        if commit:
            instance.save()
 
        return instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In our case, we don’t want to display anything except for the email and the two
password fields, so we create a ‘Meta’ class and add the fields list and the
exclude list.

Next, we need to add a custom method to do the data cleaning on the two password
fields and check that the values are valid – our validation logic here is just
that the two fields must match, but in a real-world you might have additional
validation logic (e.g. minimum length, not the same as the email, etc…).

And finally, we override the default save method.

**Why override save?**

As you saw earlier, we have derived the User model from the AbstractUser class
which contains the username field. This field has a unique constraint on it, so
it can’t just be left empty when we save.

It would also create a whole lot more code to just go ahead and write a
completely custom User model, so the simplest way around this is to set the
username to the email address that the user supplies which should also be
unique!  


### CREATE THE VIEWS

Create the view that handles taking the new user’s email and password and
creates the account in *accounts/views.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm
 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
 
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
 
    else:
        form = UserRegistrationForm()
 
    args = {'form': form}
    args.update(csrf(request))
 
    return render(request, 'register.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### CREATE THE HTML TEMPLATES

Create a file called ‘register.html’ in templates, with the following contents:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load bootstrap_tags %}
{% block content %}
    <form role="form" method="post" action="{% url 'register' %}">
        <legend>Create a new account</legend>
        {% csrf_token %}
        {{ form | as_bootstrap }}
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Create account</button>
        </div>
    </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### GETTING IT RUNNING

There’s still a few things we need to take care of to actually get the
Registration Functionality to work. Let’s take care of those now.

-   We need to configure a URL to link to the Register view. Since you will now
    be importing ‘views’ from two different apps, you will get a collision. So,
    we need to alias the imports as follows:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from accounts import views as accounts_views
from hello import views as hello_views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   With that done, you can configure the URLS as follows:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Change the register link in ‘base.html’ to the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<li><a href="{% url 'register' %}">Register</a></li>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add the ‘hello’ and ‘accounts’ apps to Installed Apps in ‘settings.py’

-   Create the migration:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ python manage.py makemigrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Run the migration:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ python manage.py migrate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Install the ‘django-forms-bootstrap’ package (note the dashes in name)

-   Add ‘django_forms_bootstrap’ to Installed Apps in ‘settings.py’ (note the
    underscores in name)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = [
...
'django_forms_bootstrap',
 ]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### RUN THE SERVER AND CHECK YOUR WORK

Run the project, then click on the Register Link to load the User Registration
Form.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/we-are-social2.png)

  
If you use the form to register a user, you should get an error. This is because
the app is attempting to show the profile page for the new user, but we haven’t
created that yet. However, the user will be created in the Database.  


### THE PROFILE PAGE

In order to fix the error that occurs on registering a new user, we need to
create the profile page.

Create the View

-   Add a profile view to ‘views.py’ in the accounts app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def profile(request):
    return render(request, 'profile.html')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Create the ‘profile.html’ template with the following code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <h2>Success!</h2>
    <p>You are logged in as {{ user.email }} </p>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add a ‘profile’ url to ‘urls.py’

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^profile/$', accounts_views.profile, name='profile'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Run the Server and check your work.

You can now register a new user and you will get a success message, instead of
an error. Don’t use the same email address you used previously, that user
already exists.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/wearesocial3.png)

Note that there is a problem with the ‘You are logged in as’ message. We haven’t
implemented logging in yet.
