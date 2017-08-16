### CREATE A VIEW

Our next step is to create a view in our HelloWorld_app. Now let’s create the
code that speaks to the world in the long-honoured tradition.

1.  Add a view function to **views.py**:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image12.png)

  
  
  
The **say_hello** function (view) takes a request parameter and returns the text
Hello, World! via a HTTP response when it’s invoked. Django injects a request
argument value into the parameter when the function is invoked. Notice we need
to import HttpResponse in order to access the **HttpResponse()** function.

At this point the view won’t be rendered, as the project doesn’t yet know it
exists. Let’s fix that.

1.  Map the view to a URL.

We need to bind our view to a URL so that a browser request will find the view.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image13.png)

  
  
  
We import views from **HelloWorld_app** to let the urls file know where the view
lives. We then add a **url()** function to the list assigned to the urlpatterns
variable.

Test the app in a browser (make sure the webserver is running):

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image14.png)

  
  
  
Success!

Let’s have a closer look at what’s going on here:

The **url()** function allows us to bind a url request to
the **say_hello** view.

The **url()** function builds url patterns and it takes five arguments, most of
which are optional:

-   **Signature**: url(regex, view, kwargs=None, name=None, prefix=”)

-   **Example**: url(r’\^\$’, views.say_hello)

Let’s break it down:

**r** – means that the string literal (the text immediately after it in
quotations) is to be treated as a raw string, and any escape characters that
might be present are ignored.

**regex** –  this is a regular expression.

-   the **\^** sign looks for a character at the beginning of a string passed in
    the URL from the browser address bar.

-   the **\$** looks for a character at the end of a string passed in the URL
    from the browser address bar.

As there is no text between **\^** and **\$**, typing the default url
 “localhost:8000”  in our browser will render our view.

**view** –  **views.say_hello** is the name of the view to invoke.

To get a better understanding of how the **regex** parameter works, modify the
string expression in the url.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image15.png)

  
  
  
Then test the project in a browser again.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image16.png)

  
  
  
The default URL doesn’t work anymore because Django can’t find a match for a URL
request with an empty string after the port number. Change the url to include
“/stuff” and our **say_hello** view will be found again.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449675915_image17.png)

  
  
  


### SUMMARY

So we’ve created our first Django project and an associated app that proudly
says Hello, World!

We’ve learned how to:

-   Install Django

-   Create a new project

-   Create an app that will say Hello, World!

-   Register our app with the project

-   Map a view to a url

-   Run the project on Django’s built-in development web server and see the view
