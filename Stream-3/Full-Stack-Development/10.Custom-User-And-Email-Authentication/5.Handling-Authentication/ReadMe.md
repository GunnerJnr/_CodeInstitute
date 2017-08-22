Handling Authentication
=======================

##### In this unit the students will learn how to handle authentication using Django

 

### HANDLING AUTHENTICATION

Now that the hard part is done, let’s finalise our new authentication system
with a few more views to handle login, logout, and the user profile page (the
page you should see first when you login).

-   Add a login view to ‘views.py’

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from accounts.forms import UserRegistrationForm, UserLoginForm
...
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
 
    else:
        form = UserLoginForm()
 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As usual, we check for the post method and if it’s not being used, we display an
empty UserLoginForm, which is just a simple email/password form with a login
button.

If the post method is being used, we populate our form with the request.POST
info and use the forms is_valid() method to validate the input before using the
‘auth’ object to authenticate our user.



### NOTE:

Remember that we created a new class call EmailAuth in our backends.py? ‘auth’
should now be able to find this in our list of backends that we supplied in the
settings.py, and call the authenticate method on that backend for us.

 

After checking that they’re logging in with valid credentials, we check to see
that the call to authenticate returns an existing user object. If successful, we
use ‘auth’ again to access the login and establish that they’re now correctly
logged into the system before redirecting to the user profile page.

-   Create the login.html’ template with the following code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load bootstrap_tags %}
{% block content %}
    <form role="form" method="post" action="{% url 'login' %}">
        <legend>Login</legend>
        {% csrf_token %}
        {{ form| as_bootstrap }}
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Login</button>
        </div>
    </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add a login url to ‘urls.py’

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^login/$', accounts_views.login, name='login'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add a login_required attribute to the profile view, to restrict access:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Set the login url in the ‘base.html’ template:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<li><a href="{% url 'login' %}">Log In</a></li>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add UserLoginForm to forms.py

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### RUN THE SERVER AND CHECK YOUR WORK

Run the project, then click on the Log In Link to log into the site. Use one of
the email addresses and passwords created while testing the Register feature.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/wearesocial4.png)

Note that the Success message now shows the email address of the logged in user.

 

### LOGGING OUT

Set the Log Out line in ‘urls.py’

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^logout/$', accounts_views.logout, name='logout'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the Log Out link in ‘base.html’

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<li><a href="{% url 'logout' %}">Log Out</a></li>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you’ve fixed the logout link in base.html, you can add a method in
views.py to destroy a login session:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, we call on the ‘auth’ object to supply the logout method to destroy the
user session. But that’s all there is to it!  


### SUMMARY

This unit has given us an understanding of what’s involved in the whole process
of authentication and how you can configure Django to use alternative means of
authentication.
