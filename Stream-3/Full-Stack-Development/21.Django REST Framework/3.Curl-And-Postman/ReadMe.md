CURL & Postman
==============

##### In this unit the students will learn how to test their Django API using tools such as cURL and Postman

 

The two most common tools for testing APIs are **cURL** and **Postman**.

 

**cURL **is a command line tool that comes pre-installed
on **Mac** and **Linux**. It also comes pre-installed
with **Git** for **Windows** users.

 

Go ahead and open up your **command line** tool
– **Terminal** for **Mac** and **Linux** or **Git Bash** on **Windows** (do not
try to use Powershell’s curl command for this task, it’s not really curl). Once
the command line is open, run the following command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl http://127.0.0.1:8000/todo/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will give us the same information as the Django Rest Framework:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image7.png)

  
The problem here is that the information isn’t very easy to read. Fortunately
there’s a tool that comes installed with Python will allow us to pretty print
the JSON data. We can do that by running the following command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl http://127.0.0.1:8000/todo/ | python -m json.tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OK, so now we’re running two commands here! The pipe symbol ( **\|** ) here will
allow us to **pipe** the output from the first command (**curl**) into the
second command – which invokes the pretty print tool that Python provides
called **json.tool**.

 

This will give us the following:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image8.png)

  
Now the information is much easier to read! At the moment this will work fine –
but we can also use **cURL** to make a **POST** request.

Before we do that though, we’ll need to update our **TodoView** to enable the
server to handle a **POST** request. Go ahead and open the **views.py** file in
the **todo** app and add the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    def get(self, request):
        """
        Handle the GET request for the `/todo/` endpoint.
 
        Retrieve a complete list of `todo` items from the Todo
        model, serialize them to JSON and return the serialized 
        todo items.
 
        Returns the serialized `todo` objects.
        """
        todo_items = Todo.objects.all()
        # Serialize the data retrieved from the DB and serialize
        # them using the `TodoSerializer`
        serializer = TodoSerializer(todo_items, many=True)
        # Store the serialized data `serialized_data`
        serialized_data = serializer.data
        return Response(serialized_data)
 
    def post(self, request):
        """
        Handle the POST request for the `/todo/` endpoint.
 
        This view will take the `data` property from the `request` object,
        deserialize it into a `Todo` object and store in the DB.
 
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
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we’ve added our **post** method. This will handle any **POST** requests that
are made to the server.

 

On **line 44**, we instantiate a new **TodoSerializer**. This time we pass
through the data contained in the request object. This will **deserialize** the
request data.

 

After that, we check to see if the data is valid. If the **serializer** is not
valid, then we return a **response** containing the errors and the **HTTP
status** of **400**, which we imported on **line 5**.

 

An example of invalid data in this case would be if we sent across an object
that was missing a field that we specified in the **TodoSerializer**, such
as, **title**. Or, a field that isn’t present, such as **username**.

 

After that we call the **save** method on the **serializer** object. This will
save the new data to our model!

 

After that we return the **serializer data**, as well as a **HTTP
status** of **201** – which is used when something has been created!

 

Now let’s look at how we can call that URL using **cURL**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl -X POST -H "Content-Type: application/json" -d '{"title": "Add Put Request", "description": "Create a handler for the PUT request", "status": 1}' http://127.0.0.1:8000/todo/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Firstly, we need to set the request type. This time we’re using **POST** – so in
order to do that, we need to use **-X POST**.

 

Next we need to tell the server what type of content it should expect. This is
a **HTTP Header** – so in order to tell the server to expect
the **JSON** content type, we need to use **-H “Content-Type:
application/json”**.

 

After that we need to pass the data! We use **-d** and then we put
our **JSON** inside a pair of single quotes. And then we just have the same URL
as before!

 

Another tool that we can use for this is **Postman**. **Postman** is a nice
visual tool that we can use instead of **cURL** that can be installed as a
Chrome extension or as a standalone app (only on **Mac**).

 

We can download it from here: <https://www.getpostman.com/>

 

Go ahead and download it. Once it’s downloaded and installed, go ahead and
launch it. It will prompt you to register or login. You can do so if you wish,
but it is not necessary as you can also **Skip this step**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image9.png)

  
Now if we enter **127.0.0.1:8000/todo/** into the URL bar and click **send**,
we’ll get something that looks like the following:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image10.png)

  
Now let’s use **Postman** to update some information for one of the todo items.
First we’ll need to implement the functionality in our view, so let’s open up
the **views.py** in our **todo** app:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    # Code snippet truncated for brevity
 
    def put(self, request, pk):
        """
        Handle PUT request for the `/todo/` endpoint.
 
        Retrieves a `todo` instance based on the primary key contained
        in the URL. Then takes the `data` property from the `request` object
        to update the relevant `todo` instance.
 
        Returns the updated object if the update was successful, otherwise
        400 (bad request) is returned
        """
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
 
        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request response will be returned containing the error.
        # Else, save and return the data.
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we’re passing through a primary key to our **put** method. This will allow
us to determine which todo record to update.

 

We then retrieve the Todo record, where the ID is equal to the **pk** that we
passed into the **put** method.

 

Then we just tell the serializer which Todo item that we wish to update by
passing through the **todo** record that we retrieved on **line 29 **, along
with the data that we pass through in the **request** object.

 

Then we just perform the same logic tha’st used in the **post** method to check
if the **serializer** is valid. If it’s not valid, then we return a response
containing the errors and the **HTTP status**. And if the **serializer** is
valid, then we **save** the data.

 

So how do we pass that value to the **put** method? Simple – we create a new
URL.

 

So open up the the **urls.py** file in the **todo** directory and add the
following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url
from todo.views import TodoView
 
urlpatterns = [
    url(r'^$', TodoView.as_view()),
    url(r'(?P<pk>[0-9]+)/$', TodoView.as_view())
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have the URL to pass through to the **put** method. This will be handle
the same way as the methods. Once Django knows that the request is
a **PUT** request, it will invoke the **put** method on the **TodoView**.

 

Now we just need to know how to invoke the URL using **Postman**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image11.png)

  
First we need to select **PUT** from the dropdown menu next to the URL bar.

 

After that we put the URL we wish to call in the URL bar. In this case, we
use **127.0.0.1:8000/todo/1/**. **1** is the ID of the todo item that we wish to
update.

 

Now under the URL bar we have a number of tabs. Go ahead and click on
the **Body** tab. This section will allow us to enter
the **key/value** **pairs** that we wish to pass to the server as our **request
data**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image12.png)

  
Here we’re just updating the first record to set the status to **3**, which
is **Done**. Go ahead and click on the **Send** button to send the request. Once
that’s done we should get the following response:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/11/1479225809_image13.png)

  
That’s it – we’ve managed to update one of our todo items!

 

Now that we know how to access the API through **cURL** and **Postman**, and
access the server using different **HTTP methods**, we can now create
a **delete** method and we can also modify the existing **get** method so we can
get single todo records by the ID.

 

Let’s open up the **views.py** file in our **todo** app and update our code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo
 
 
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to 
    `todo` items
    """
 
    def get(self, request, pk=None):
        """
        Handle the GET request for the `/todo/` endpoint.
 
        Checks to see if a primary key has been provided by the URL.
        If not, a full list of `todo` will be retrieved. If a primary key 
        has been provided then only that instance will be retrieved
 
        Returns the serialized `todo` object(s).
        """
        if pk is None:
            todo_items = Todo.objects.all()
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
 
    # Code snippet truncated for brevity
 
    def delete(self, request, pk):
        """
        Handle DELETE request for the `/todo/` endpoint.
 
        Retrieves a `todo` instance based on the primary key contained
        in the URL and then deletes the relevant instance.
 
        Returns a 204 (no content) status to indicate that the item was deleted.
        """
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On **line 16** we’ve updated the signature of our **get** method to take the
argument of **pk** and set the default value to **None**.

 

Then we’ll do a check to see if the **pk** is **None**. If it is **None**, then
we’ll go ahead and retrieve all of the todo items just as before. If it is
not **None**, then we’ll retrieve the todo that has that ID and we’ll serialize
that **Todo** instance. This will allow us to make a **GET** request
to **http://127.0.0.1:8000/todo/** to retrieve all of the **todo** records.

 

Or, we’ll be able to make a **GET** request
to **http://127.0.0.1:8000/todo/1/** to retrieve the **todo** record with
an **ID **of **1**.

 

On **line 45** we’ve created a **delete** method. This method takes in
the **pk** argument so we can make a **DELETE** request to delete a specific
todo item based on its ID.

 

Inside the **delete** method, we just retrieve a todo item based on its ID and
then we delete that item.

 

Lastly, we return a **status** of **HTTP_204_NO_CONTENT**. This will return the
status to inform the client that there is no longer a record with the ID that
was passed to the server.

 

 **COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/django-todo/part_3/django_todo>
