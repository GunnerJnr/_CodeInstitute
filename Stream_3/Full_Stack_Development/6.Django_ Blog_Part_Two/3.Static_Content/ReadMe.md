###  

### ADD STATIC CONTENT

Similar to our approach to templates, production level web applications tend to
have static content; that is, content that does not dynamically store within
files in locations that can be accessed by the entire site, such as CSS and
JavaScript.

Django is set up for this and will look for static content in a directory
specified in our project settings file. We:

1.  Create a new directory in your project root called **static**.

2.  Create a subdirectory inside static called **css**.

3.  Update **settings.py** so it can see the new static directory and all its
    subdirectories. Add **STATICFILES_DIRS** below the already
    included **STATIC_URL** setting:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STATIC_URL = '/static/'
 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Create a new file called **blog.css** that we’ll use to style our blog.

2.  Save the file to the css folder.

3.  Add some style rules to test:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
body {
    font-family: Arial;
}
 
h1 a {
    color: #555555;
    text-decoration: none;
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our base template needs to know where to find the css content. To do this, we
need to add two template language elements to our **base.html** file. The first
is an instruction at the top of the file to include static files, which will
point to our static folder that we just created and configured. The second is a
link to the css file we added to the css directory.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head>
    <title>Bootcamp Blog</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/blog.css' %}">
</head>
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fire up the web server again and you should see the styles applied to our code.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449510693_image2.png)

 

### LET’S ADD MORE STYLING TO OUR BLOG

We’d like our blog a bit more interesting, something like below:  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449510693_image3.png)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify blog.css to include the style rules below:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.navbar-form input, .form-inline input {
    width: auto;
}
 
body {
    font-family: Arial;
    padding-top: 50px;
}
 
footer {
    margin-top: 40px;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #ededed;
}
 
h1, h1 a {
    color: #555555;
    text-decoration: none;
}
 
#masthead {
    padding-left:10px;
    min-height: 199px;
}
 
#masthead h1 {
    font-size: 55px;
    line-height: 1;
    margin-top: 50px;
}
 
#masthead .well{
    margin-top: 31px;
    min-height: 127px;
}
 
.navbar.affix {
    position: fixed;
    top: 0;
    width: 100%;
}
 
#logo {
    color: #12AB82;
}
 
.story-img {
    margin-top: 25%;
    display: block;
}
 
a, a:hover {
    color: #223344;
    text-decoration: none;
}
 
.icon-bar {
    background-color: #fff;
}
 
.dropdown-menu {
    min-width: 250px;
}
 
.panel {
    border-color: transparent;
    border-radius: 0;
}
 
.thumbnail {
    margin-bottom: 8px;
}
 
.img-container {
    overflow: hidden;
    height: 170px;
}
 
.img-container img {
    min-width: 280px;
    min-height: 180px;
    max-width: 380px;
    max-height: 280px;
}
 
.txt-container {
    overflow: hidden;
    height: 100px;
}
 
.panel .lead {
    overflow: hidden;
    height: 90px;
}
 
.label-float {
    margin: 0 auto;
    position: absolute;
    top: 0;
    z-index: 1;
    width: 100%;
    opacity: .9;
    padding: 6px;
    color: #fff;
}
 
@media screen and (min-width: 768px) {
    #masthead h1 {
        font-size: 80px;
    }
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then modify **base.html** to use the new CSS styles:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head>
    <title>Stack - BootCamp Blog</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.6/cerulean/bootstrap.min.css">
    <link rel="stylesheet" href="{% static "css/blog.css" %}">
</head>
<body>
<div id="masthead">
    <div class="container">
        <div class="row">
                <h1> stack
                    <p id="logo" class="lead">The Trials of a Bootcamp Developer</p>
                </h1>
        </div>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel">
                <div class="panel-body">
                    <!--blog entries-->
                    {% block content %}
                    {% endblock %}
                    <!--blog entries-->
                </div>
            </div>
        </div>
    </div>
</div>
<footer>
    <div class="container">
    </div>
</footer>
<!-- script references -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fire up the server again to test your changes.  


 **COMPLETED CODE**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Three/Unit06-Django_Blog_Part2/blog_prj>  


### SUMMARY

In this lesson we learned how to:

-   Add views and templates needed for a non-admin user to read the blog.

-   Create a more flexible site architecture.

-   Add static content to our projects.
