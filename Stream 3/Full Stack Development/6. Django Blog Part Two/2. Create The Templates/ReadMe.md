### CREATE A SITE-WIDE TEMPLATE DIRECTORY

What if we want all our apps to inherit from the same base template? Well, in
that case the easiest thing to do would be to place our template directories and
files outside of any particular app. We don’t actually need to do this yet as
our blog only has one app associated with it, but we will need to do this on
later projects and now is as good a time as any to learn this).

   
The steps below don’t apply if you are using Pycharm as your IDE. Pycharm
automatically creates the project-level templates directory and updates
settings.py for you when you create a new Django project.

  
So what do we need to do to make this happen?

1.  Create a new folder called **templates** in our project root.

2.  Let **settings.py** know where templates lives. Modify **‘DIRS’** to include
    the project root directory concatenated with the templates subdirectory.
    This is done on **line 4** below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### CREATE A NEW BASE TEMPLATE

Create a new file called **base.html** in our templates directory and add the
following to the file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<html>
    <head>
        <title>Bootcamp Blog</title>
    </head>
    <body>
        <div>
            <h1><a href="/">Bootcamp Blog</a></h1>
        </div>
        <div>
            <div>
                <div>
                    {% block content %}
                    {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The link inside the **\<h1\>** tag will eventually contain a link to a **blog
post detail** view.  


### CREATE A CHILD TEMPLATE

As you might guess, most of the blog’s dynamic data will be displayed from a
child template. And to do that, we’ll create some template code that can receive
a QuerySet from the view. Let’s make one now.

1.  Create a new child template file called **blogposts.html**:  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
 
{% block content %}
    {% for post in posts %}
        <div>
            <div>
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.content|linebreaks }}</p>
        </div>
    {% endfor %}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fire up the server and use the following url to access the
blog: **localhost:8000/blog**

You should see something like this:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449510693_image1.png)

  
The content and basic structure are in place, but it still won’t win any UX
awards. Let’s address that now by styling the blog.
