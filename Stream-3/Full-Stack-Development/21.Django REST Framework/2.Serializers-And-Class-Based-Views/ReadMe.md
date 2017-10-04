Serializers & Class-Based Views
===============================

 

Now that we’re set up, we can create, view, update, and delete todo items from
the admin panel. Now we just need to update our code so we can do all of
this *without* the admin panel!

 

This means that we need to create some views. But before we can create the
views, we need to create our **serializer** so our view will be able
to **serialize** the data!

 

In order to do this, we need to create a new file in our **todo** app
called **serializers.py**. Inside that file we’ll add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from rest_framework import serializers
from todo.models import Todo
 
 
class TodoSerializer(serializers.ModelSerializer):
    """
    Todo Serializer.
 
    Used to serialize the Todo model to JSON. The fields to be 
    serialized are:
    - id
    - title
    - description
    - status
    - updated
    """
 
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description',
                  'status', 'updated')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So here we’re importing the **serializer** module from the Django Rest
Framework, as well as our **Todo** model.

 

Next we define our **TodoSerializer** which inherits from
the **ModelSerializer** class provided by the Django Rest Framework.

 

Inside the class definition, we create a **Meta** class. This is where we’ll
tell the Django Rest Framework what model we want to **serialize**, as well as
the fields that we want to be **serialized**.

 

In this instance, we are choosing to **serialize** the **Todo** model and
the **id**, **title**, **description**, **status**, and **updated** fields.

 

Now let’s create our new view. Up until now, we’ve been working with Django’s
function based views. This time, however, we’re going to look at a class based
view, or **CBV**.

 

**CBV**s allow us to inherit functionality from another base **CBV**. We’ll add
the following in the **views.py** file of our **todo** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.serializers import TodoSerializer
from todo.models import Todo
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    def get(self, request):
        """
        Retrieve a complete list of `todo` items from the Todo
        model, serialize them to JSON and return the serialized 
        todo items
        """
        todo_items = Todo.objects.all()
        # Serialize the data retrieved from the DB and serialize
        # them using the `TodoSerializer`
        serializer = TodoSerializer(todo_items, many=True)
        # Store the serialized data `serialized_data`
        serialized_data = serializer.data
        return Response(serialized_data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Here we import the **Response** and **APIView** classes from the Django Rest
Framework.

 

After that we’re just importing the **TodoSerializer** and **Todo** model.

 

Next we define our **TodoView**. This class will inherit from the **APIView**.
This **APIView** comes with all the pre-built functionality required to return
a **serialized response**.

 

In order to be able to access this data we’ll need to create a new method
called **get**.

 

The reason that we’ve called this method **get** is because when we make
a **GET **request to the server, it will automatically invoke
the **get** method.

 

Inside the **get** method, we retrieve all of the **Todo** records. After that,
we instantiate the **TodoSerializer** object by passing through the todo records
that we retrieved. We also need to set the **many** argument to **True**. This
will inform the **serializer** that there’s multiple records to
be **serialized**.

 

This will store the data in the **.data** property of the **serializer object**.

 

On **line 25** we store this data in a variable called **serialized_data** to
improve the readability.

 

After that we return an instance of the Django Rest
Framework’s **Response** object. This will contain the serialized data!

  
So let’s hook up everything now with our URLs. Create a new file inside
the **todo** app called **urls.py**. And inside that new file add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url
from todo.views import TodoView
 
urlpatterns = [
    url(r'^$', TodoView.as_view())
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Here we just import the **TodoView** from the todo app. Then we add a new URL
to **urlpatterns**. When we’re creating a new url for the **TodoView**, we need
to invoke the **as_view** method on the **TodoView**.

 

Any view that inherits from the base **View** object will have
the **as_view** method. This will allow Django to use the class-based view as a
standard function-based view.

 

Next, open up the **urls.py** file in the **django_todo** directory and add in
the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url, include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', include('todo.urls'))
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### NOTE

When we expose the URLs of an API, we refer to them as **endpoints**. This is
how a client application will gain access to our server. This is merely a matter
of terminology, but keep it in mind!

 

Let’s open this up in our browser and head over
to **http://127.0.0.1:8000/todo/**

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image6.png)

 

The great thing about Django Rest Framework is that it gives us the interface to
access the API without relying on external tools.

 

As we can see above, there are two records in the database – and each of the
fields that we specified in the **TodoSerializer** are present.

 

But what if the backend isn’t written with the Django Rest Framework? In that
case, we’ll be able to test the API with other tools!

 

**COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/django-todo/part_2/django_todo>
