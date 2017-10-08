###  

User Authentication
===================

 

Now that we’ve created the API, we need to allow users to register and login.
This will allow users to create, edit, view, and delete todo items. In order to
do this, we need to be able to **authenticate** users.

 

Previously we were able to **authenticate** users using Django – but this time
around we can’t really on Django because we’re not relying on Django’s forms or
Django’s means of keeping users **authenticated**.

 

We can do this by a variety of approaches. The most common ways of doing this by
using **OAuth tokens** or **JWTs**. Both of these can be used to determine
whether or not a user is allowed to be accessing the API.

 

In this lesson we’re going to be using **JWTs**. The reason we’re going
with **JWTs** is because they’re easy to work with and have become a more modern
way of verifying API access. So without further ado, let’s get started!

 

First we’ll need to install some stuff – Python packages to be specific. We’ll
need to install the following:

-   pyJWT==1.4.2

-   djangorestframework-jwt==1.8.0

These can either be installed from the command line or in Pycharm – just make
sure you install the versions noted above!

 

After that we’ll need to create a new **Django app** called **accounts**. This
is where we’ll keep all of the code for the authentication process. We’ll start
by creating the **serializer**. Create a new file called **serializers.py** and
add the following code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from rest_framework import serializers
from django.contrib.auth.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
 
    Handles the serialization of the `User` model.
 
    The fields to be serialized are:
    - username
    - password
    """
 
    class Meta:
        model = User
        fields = ('username', 'password')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we’re just creating a
new **ModelSerializer** called **UserSerializer**, just like we did in
the **todo** app.

 

This time we’re creating a serializer for the **User** model and we’re only
serializing the **username **and **password** fields.

 

In **views.py** file of our **accounts** app, we’ll add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
 
 
class UserView(APIView):
    """
    UserView handles the requests made to `/accounts/`
    """
 
    def post(self, request):
        """
        Handles the POST request made to the `/accounts/` URL.
 
        This view will take the `data` property from the `request` object,
        deserialize it into a `User` object and store in the DB.
 
        Returns a 201 (successfully created) if the user is successfully
        created, otherwise returns a 400 (bad request)
        """
        serializer = UserSerializer(data=request.data)
 
        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request response will be returned.
        # Else, save the data and return the data and a successfully
        # created status
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            # Create a new user using the `username` contained in 
            # the `data` dict
            user = User.objects.create(username=data["username"])
            # Use the `set_password` method to create a hashed password
            # using the password provided in the `data` dict
            user.set_password(data["password"])
            # Finally, save the new `user` object
            user.save()
            return Response(data, status=status.HTTP_201_CREATED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is pretty much more of the same as what we done in our **todo** view. The
difference is that on **line 36**, we save all of our serialization data in a
variable called **data**. Then we create a new **User** on **line 39** and we
pass through the **username**.

 

After that we need to invoke the **set_password** method and pass through the
password contained in the **data** variable. The reason that we need to call
the **set_password** method is because the **set_password** method will hash
the **password**, so it won’t be stored in plain text!

 

Next we need to create some URLs for our **accounts** app. Go ahead and create a
new **urls.py** file inside the **accounts** app and add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import UserView
 
urlpatterns = [
    url(r'^register/$', UserView.as_view()),
    url(r'^api-token-auth/$', obtain_jwt_token)
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have our URL for our **UserView**.

 

On top of that, we’ve also created a URL for **accounts/api-token-auth/**. This
URL will invoke a **view** called **obtain_jwt_token**. This view is provided by
the **djangorestframework-jwt** package that we installed earlier and we
imported it on **line 3**.

 

So for our **UserView** we’ll need to provide a **username** and **password**.
The same is true for the **obtain_jwt_token** view. The **UserView** will create
the new user and store their information in the database and
the **obtain_jwt_token** view will create a **JWT** based on
the **username** and **password**. This will basically act as our **login** URL.

 

Now we just need to update our URLs, so open up the **urls.py** file in
the **django_todo** directory and add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', include('todo.urls')),
    url(r'^accounts/', include('accounts.urls'))
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Let’s go ahead and open up **cURL** to create a new user and then we’ll retrieve
the JWT:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl -X POST -H "Content-Type: application/json" -d '{"username": "timmy", "password": "password"}' http://127.0.0.1:8000/accounts/register/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will return the **username** and **password**. After that we will make the
call to retrieve our JWT:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl -X POST -H "Content-Type: application/json" -d '{"username": "timmy", "password": "password"}' http://127.0.0.1:8000/accounts/api-token-auth/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will respond with our JWT!

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image14.png)

  
So we can get a token, so what? At the moment that doesn’t actually make any
difference because we have to block any requests that are made to
our **todo** URL that don’t have permission to access them! But why are we doing
this?

 

Well, imagine our application is a secure building. We can let pretty much
anyone in through the front door. Once someone walks in the door, they sign in
at reception. Once they’ve signed in, they’re given a keycard and this keycard
will give that person access to certain areas of the building.

 

So if we were to build a secure building, we need to lock down certain parts the
building. We also need to determine how long our keycard can be used for.

 

Open up the **settings.py **file so we can put this security in place! After
the **INSTALLED_APPS** setting, add in the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
 
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have our security in place. These are the default permission and
authentication classes provided by the Django Rest Framework and Django Rest
Framework JWT.

 

Then after that we have our **JWT_AUTH** settings. In there we set
the **JWT_ALLOW_REFRESH** to **True**. All tokens will expire after a certain
amount of time. After a token expires, it can be refreshed – so here we’re
saying that we want to be able to refresh the tokens.

 

Next we set **JWT_REFRESH_EXPIRATION_DELTA**. We set this to 7 days. Just
remember to **import datetime**!

 

Try to make a **cURL** request to register a new user. Still works, right?
Indeed it does! Which is good because we want all our potential users to be able
to register.

 

However, we don’t want all of our users to be able to access the todos, so we
need to block access to that view.  
To do that, we need to add the following to the **views.py** file in
the **todo** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from todo.serializers import TodoSerializer
from todo.models import Todo
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    permission_classes = (IsAuthenticated,)
 
    # Code truncated for brevity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now on **line 6** we are importing the **IsAuthenticated** class from the Django
Rest Framework.

 

Then on **line 17** we need to set our **permission_classes**. Inside that
tuple, we add the **IsAuthenticated** class.

 

Next, we’ll need to add a similar line of code to our **UserView**. The reason
for this is, once we introduce permissions, all of the views will locked down
and we won’t be able to access any of them without permissions. We don’t
actually need any permission to access the **UserView**, but Django will
complain if don’t set the **permission_classes**, so let’s do that now.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
 
 
class UserView(APIView):
    """
    UserView handles the requests made to `/accounts/`
    """
 
    permission_classes = ()
 
    # Code snippet truncated for brevity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now try to access the **TodoView** by using the following **cURL** command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl http://127.0.0.1:8000/todo/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now we’re getting an error telling us that our authentication details were not
provided:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image15.png)

  
So how do we provide them? Well, we need to add the **Authorization header** to
our **request**.

 

First retrieve the auth token by calling
the **http://127.0.0.1:8000/accounts/api-token-auth/** by passing your
user’s **username** and **password** as the data.

 

Once you get the response back, run the following command (with the username you
want to retrieve todos for:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl -H "Authorization: JWT <your JWT>" http://127.0.0.1:8000/todo/2/?username=admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And there we go!

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image16.png)

  
But now we need to link our todo items to our users. In order to do that, we
need to update our **Todo model**, as well as our **get** and **post** methods.

 

We’ll go for the model first. Open up **models.py** in our **todo** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
 
# Two-sequence containing the different possible
# states of a todo item
STATUS_CHOICES = (
    ('Todo', 'Todo'),
    ('Doing', 'Doing'),
    ('Done', 'Done')
)
 
 
class Todo(models.Model):
    """
    Todo model.
 
    Contains the `user`, `title`, `description`, `status` and `updated` fields
    for a Todo item
    """
 
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, null=False)
    updated = models.DateTimeField(default=timezone.now)
 
    def __unicode__(self):
        return self.title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now this will present a bit of a problem. The **user** field cannot be null,
which means that all of the existing will need to be given a user. In order to
address this, we’ve set the default to **1** on **line 24**.

 

Note also that we need to change the **max_length** property of
the **status** model to **5** to cover the new values.

 

Go ahead and run the **makemigrations** command, followed by
the **migrate** command. Notice that we’ve also updated
the **STATUS_CHOICES** and replaced the numbers. We’ve just done this for
readability – so when we retrieve the information from the API, we actually know
what the **status** is instead of just seeing a number. Unfortunately, this
means that we’re going to have to head into the admin panel and update these
changes on each of the existing **Todo** items.

 

Alternatively, you could update these by using **cURL**.

 

Now that we’ve got the difficult part out of the way, we need to update
the **views.py** file.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from todo.serializers import TodoSerializer
from todo.models import Todo
from django.contrib.auth.models import User
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    permission_classes = (IsAuthenticated,)
 
    def get(self, request, pk=None):
        """
        Handle the GET request for the `/todo/` endpoint.
 
        Gets `username` from the `query_params` in order to retrieve the
        `todo` items belonging to that user, then checks to see if a primary key has been provided by the URL.
        If not, a full list of `todo` will be retrieved. If a primary key 
        has been provided then only that instance will be retrieved.
 
        If no username was found in the `query_params` then a 404 (not found)
        error will be returned
 
        Returns the serialized `todo` object(s).
        """
        if "username" in request.query_params:
            if pk is None:
                # Get the `user` based on the username provided by the
                # `query_params`
                user = User.objects.get(username=request.query_params["username"])
                # Filter the `todo` items based on this `user`
                todo_items = Todo.objects.filter(user=user)
                # Serialize the data retrieved from the DB and serialize
                # them using the `TodoSerializer`
                serializer = TodoSerializer(todo_items, many=True)
                # Store the serialized data `serialized_data`
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                # Get the object containing the pk provided by the URL
                todo = Todo.objects.get(id=pk)
                # Serialize the `todo` item
                serializer = TodoSerializer(todo)
                # Store it in the serialized_data variable and return it
                serialized_data = serializer.data
                return Response(serialized_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
    def post(self, request):
        """
        Handle the POST request for the `/todo/` endpoint.
 
        This view will take the `data` property from the `request` object,
        deserialize it into a `Todo` object and store in the DB
 
        Returns a 201 (successfully created) if the item is successfully
        created, otherwise returns a 400 (bad request)
        """
        serializer = TodoSerializer(data=request.data)
 
        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request response will be returned containing the error.
        # Else, save the data and return the data and a successfully
        # created status
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            # Get the `user` based on the request data (not in the serializer)
            user = User.objects.get(username=request.data["username"])
 
            # Get the todo item data from the serializer
            data = serializer.data
            # Create the new `todo` item
            Todo.objects.create(user=user, title=data["title"],
                                description=data["description"], status=data["status"])
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
 
    # Code snippet truncated for brevity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we’ve updated the **get** and **post** methods. Firstly, we’ve implement a
new check to the check to see if there’s username contained in the **query
parameters**. We can access the **query parameters** by using
the **request.query_params**. in the GET request and **request.data** in the
POST request.

 

For the GET requests, our URL with the query parameter should look like this:

`http://127.0.0.1:8000/todo/?username=`

 

The server will read everything after the **question mark** as the **query
params** and will treat them as `key/value pairs.`

 

Here’s an example of how you would use this in **cURL** (and note that you’d
need to provide the username parameter similarly when using the browser to make
requests too):

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image17.png)

  
If the request doesn’t contain a query param, then a **404** will be returned.
If the **query_params** does contain a **username**, then it will check to see
if there’s a **pk** value. This will behave in the same way as before.

 

We don’t really need to search for the user here because we have a specific ID
for the todo item. However, if there is no **pk** then we need to find all of
the **todos** specific to that user – so we query the **User model** in order to
find the user that has the **username** that was contained in the **query
param**.

 

Then we query the **Todo model** to retrieve all of the **todos **that are
associated with that **user**.

 

Next, in our **POST** method we’re taking the **username** from
the **request.data**, which is available on all POST requests.

 

We need this in order associate the new **todo** with a **user**.

  
Because of this, we need to remove the **serializer.save()**. Instead we query
the **User model** and retrieve the user with the **username** contained in
the **request.data**.

 

We then manually invoke the **create **method on the **Todo model** using the
data from the **serializer**.  
  


 **COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/django-todo/part_4/django_todo>
