### CREATE A BLOG POST FORM

Now that we have the ability to upload an image, we’re going to create a blog
post creation form that users can access without having to log into the admin
screen. We’ll take advantage of Django’s built-in ModelForm functionality to
help us out on this task. More Django goodness!

To do this:

1.  Create a **forms.py** file to add selected model fields to the form.

2.  Create new views to render the form.

3.  Add a new url pattern to our project level **urls.py**.

4.  Create a new template for submitting new posts.

5.  Add the 3rd party **django-forms-bootstrap** library to dress up the form
    display.

6.  Make the post content in our **postdetail** template editable.

7.  Enable saving of new posts.

8.  Enable editing of existing posts.

 

### CREATING THE FORM

Django forms are created in a file called **forms.py**. We’re going to add one
to our blog app now.

1.  Create a new file called **forms.py** and add it to our blog app.

2.  Add the code that you see below to the file.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from .models import Post
 
 
class BlogPostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        fields = ('title', 'content','image')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s new in here?**

The **BlogPostForm** class inherits **ModelForm**, and it will create an
instance of a form when instantiated. On **line 8**, we can see that the form is
tied to the **Post** model, so that is where the form will get its data types
from.

On **line 9**, we specify the fields to be displayed. In this case we only want
the user to specify a:

-   title

-   content

-   image

We will automatically set the published and created dates in a save function in
few steps’ time.

 

### CREATE A NEW VIEW

Let’s add a view to render our model form.

Import the **BlogPostForm** class.

Create a view called **new_post**. This view creates an instance
of **BlogPostForm** and passes it to a template
called **blogpostform.html** that we will soon create.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import BlogPostForm
...
def new_post(request):
    form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### ADD A NEW URL PATTERN

We need Django to find our upcoming form template, so let’s give it a url
pattern. Add the code below to **blog/urls.py**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### CREATE A TEMPLATE FOR SUBMITTING NEW POSTS

Create and save a template file called **blogpostform.html** to the template
directory.

Code it up like below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <h1>New post</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-info">Save</button>
    </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s new in here?**

Our form template tags are contained within an HTML form tag, much as you might
expect.

The **csrf_token** is security measure to prevent [Cross Site Request
Forgery](https://docs.djangoproject.com/en/stable/ref/csrf/).

The **form.as_p** is a nifty feature that will automatically render all the form
fields you specified in the **BlogPostForm **class. And lastly there’s a button
to submit and save your blog post.

Fire up the server and enter this url to test our form:
 **http://localhost:8000/post/new/**

You should see something like this. It is not overly exciting yet, really. The
formatting isn’t the best, but we can work on that.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image4.png)

 

### INSTALL DJANGO-FORMS-BOOTSTRAP TO MAKE DELICIOUS FORMS

Luckily, there are packages out there that can help us improve the look of our
forms. A good one is **django-forms-bootstrap**.

-   Let’s install it now using **pip**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install django-forms-bootstrap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add it to the **INSTALLED_APPS** tuple.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog',
    'django_forms_bootstrap',
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Make a quick modification to our **blogpostform** template. On **line 3**,
    we load the **bootstrap_tags** and on **line 7** we specify the
    form **as_bootstrap** to implement the custom package we just installed. We
    also modified the title as a little bit of a presentation refactor.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
        {% load bootstrap_tags %}
        <h1>Add A Post</h1>
        <form method="POST">
                {% csrf_token %}
                {{ form | as_bootstrap}}
                <button type="submit" class="btn btn-info">Save</button>
        </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fire up the server and see the new changes.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image5.png)

  
Looks a lot nicer, doesn’t it? Next, we’ll wire it up so we can save our
changes.

 

### SAVE THE FORM CONTENT

As you by now know, forms are submitted using either **GET** or **POST**.

We’ll submit our form using **POST HTTP** method. In fact, we already specified
that when creating our template as you can see on **line 5** below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
        {% load bootstrap_tags %}
        <h1>Add A Post</h1>
        <form method="POST">
                {% csrf_token %}
                {{ form | as_bootstrap}}
                <button type="submit" class="btn btn-info">Save</button>
        </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We would like to redirect to the **postdetail** template once we have saved our
post, just to see our newly created blog post entry.

To save our posts, we need to first modify the **new_post** view that we created
earlier in the lesson.

The code to do this is shown below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import redirect
...
def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default **HTTP** method for accessing web pages is via **HTTP GET**.

When we navigate to our form view to add a new post, we will do so via **GET**.
However, a **HTTP POST** method is used when we save a post that refreshes upon
the save action recognized by the browser. This is why the **if-statement** is
in place:

If the view was accessed because the **Submit** button was clicked, then it will
become true that the request method is **POST**. 

1.  The form data will be saved to the database.

2.  Once the data is saved, we will be redirected to the **postdetail** view.

Else if view was opened from a link, then:

1.  The **GET** method has seen to have been used.

2.  The new post form is displayed.

If the method is **POST**, then we want to create a new instance
of **BlogPostForm** from the data passed from the HTML form.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
form = BlogPostForm(request.POST)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We then check if the form is valid. In other words, we ensure that the blog post
title and content fields contain some text. If they do, then:

-   We save the form to a new variable called **post** which will hold an
    instance of the **Post**model (not to be confused with **HTTP POST**). We
    don’t commit (**commit = False**) just yet, because the **Post** model
    requires an author value to be non-null when saving to the database.  

We temporarily hold off on saving until we get:

-   The **user**, which is automatically supplied if the user is logged in to
    the project. We can only do this by logging in to the admin page for now.

-   The **published date** which is the current time.

If we are not logged in, we’ll get the following error:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image6.png)

  
So make sure to log in to the admin screen when testing. We’ll fix that in a
later lesson when we learn how to register new users from the front end.

-   We then save our post.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Once we have saved our new post, we redirect back to
    the **postdetail** template and pass the newly created **post primary
    key** to let the view know which post is to be displayed.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 return redirect(post_detail, post.pk)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

However, if we just linked to the new post view from another location, all the
above code within the body of the **if-statement** is ignored and the **else
statement** block is executed. The empty form is displayed to the user, ready to
take data and create a new post.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
else:
    form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An extra bonus is that Django forms come with built in validators. Try and save
a post without any text in the fields and you’ll see. We are implementing good
practices here, by validating in the browser and also on the
server **(is_valid())**

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image7.png)

 

### ENABLE SAVING OF AN IMAGE

We have two more things to do to get our new post saved correctly. If we try to
save an image as part of the blog post, it won’t get saved. Django won’t throw
an error either.

So what do we need to do?

-   Add an **encoding** type to our HTML form. This tells the request to look
    for an attached file travelling with the form data.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<form method="POST" enctype="multipart/form-data">
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add a new parameter to the **BlogPostForm** constructor within new_post that
    passes in the image file.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
form = BlogPostForm(request.POST, request.FILES)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test your changes by creating a post with an attached image.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image8.png)

 

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image9.png)

 

### EDITING AN EXISTING BLOG POST

Updating an existing post isn’t too much different from adding a new post:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s new in here?**

This looks very much like our **new_post** view we created earlier. But there
are a few differences which you no doubt spotted when typing out the code. The
function take a **primary key id** as an extra parameter (just like
the **post_detail** view).

Editing an item using a form is a two step process. First we need a way to get
the item we want to edit into a Form in the browser. Then we want to process the
edit when the user clicks submit.

Getting the Initial form is achieved using a **HTTP GET** method. Handling the
submitted changed is acheived using a **HTTP POST** method.

Our **edit_post** view above handles both these scenarios and uses **if
request.method == “POST”:** to decide which is happening.

If the method is **POST** then we must take the submitted details, validate
them, save them to the database, and then redirect the user to the page that
will show them the edited post.

As with the **‘new_post’** view, we need to add support for images to be
attached to the blog post.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
form = BlogPostForm(request.POST, request.FILES, instance=post)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the method is **GET** then we just instantiate the **BlogPostForm** giving it
the post we’re editing, and direct the user to it.

Now, add an ‘**Edit**’ button to the post details template, after the ‘**Back To
Blog**’ button:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<button class="btn btn-default" onclick="location.href='/blog'">Back To Blog</button>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<button class="btn btn-default" onclick="location.href='{% url 'edit' post.id %}'">Edit</button>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice that the href is simply ‘**edit**’. This is a relative link to the
current post, so it will cause a **GET**method, and the url will become the the
url of the post with ‘**/edit**’ appended at the end.

Now we just have to link that edit url to the view method we created above. Add
a url pattern to the **‘urls.py’** file in the blog app.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**And finally…**

We didn’t add a button anywhere to actually open the new post form. We can only
do that by entering the URL. Let’s fix that.

Add a button to the **‘blogposts.html’** file. See if you can figure out the
best place to put it.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<button class="btn btn-default" onclick="location.href='{% url 'new_post' %}'">New Post</button>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### SUMMARY

In this lesson, we:

-   Added a post submission form to allow users to add new blog posts without
    having to go through the admin interface to do so.

-   Added the ability to upload and display images on blog posts in order to
    make the blog stories more visually appealing.

-   Used the `name = ' ' `syntax in your urls to enable the `{% url ' '
    %}` links for html buttons.
