Creating Content Pages
======================

##### In this unit the students will learn how to create content for their flatpages using Django's admin panel

 

### CREATING CONTENT PAGES

Now that we’ve configured the flatpages system, we can go ahead and add some
content using the admin.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image4.png)

  
Click   

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image5.png)

    on the “Flat pages” row to create a new page and start editing your content.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image6.png)

   
Note that there are two sites. example.com was created automatically, we added
localhost. This is why we specified a SITE_ID of 2 earlier.  
If you have any issues, note that based on the exact way you set up your site,
it might have a higher id (most likely 3); take a look at the django_site table
in the database for the value to use.

The  URL must contain the ‘/pages/’ prefix, (in our example we’re using
‘/pages/about/’ and enter some text for the title and content).

Finally, choose the site, which in our case is localhost. But in practice, you
may have a few in this list. These would normally be selected by CTRL-Clicking
each one.

We’re going to ignore the advanced options for now, but we’ll be taking a look
at them very shortly when we start to customise our flatpages behaviour.

Finish by clicking    

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image7.png)

Now we can test our new page by starting our server and browsing to:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
http://127.0.0.1:8000/pages/about/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the Server and enter the URL to test:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image8.png)

### ADD A TEMPLATE

The about page you created above does it’s job, but it’s just plain text. It
would not fit the overall look and feel of a larger site. In this section we
will create a base template that can be used to style all pages in a site, and
we’ll see how easy it is to apply that style to flat pages.

### CREATE THE BASE TEMPLATE

-   In the templates directory, create a html file called base.html with the
    following html:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Our Simple Site</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.6/cerulean/bootstrap.min.css">
    <link rel="stylesheet" href="{% static "css/style.css" %}">
</head>
<body>
<div class="container">
   <div class="masthead">
       <ul class="nav nav-pills pull-right">
           <li><a href="#">Home</a></li>
           <li><a href="#">About</a></li>
           <li><a href="#">Contact</a></li>
       </ul>
       <h1><span class="fui-settings-16 muted">Our Simple Site</span></h1>
   </div>
 
   <hr>
 
   <div class="container">
       {% block content %}
       {% endblock %}
   </div>
 
   <hr>
 
   <div class="footer">
       <p>Made By Bootcampers and Django </p>
   </div>
</div>
</body>
 
<!-- script references -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"> 
</script>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Change the index.html file to see the template applied to the landing page
    of the site. Replace the existing code with the following:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends 'base.html' %}
{% block content %}
    <h2>Hello, World!</h2>
    <p>Our very simple site</p>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Run the server and visit the landing page. Notice that even though the
    index.html file only contains minimal content, it has been wrapped in the
    content and styling from base.html.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/we_are_social.png)

 

-   Visit the About Page at /pages/about/. Note that it is still styled as
    plaintext. It does not extend the base template.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455289439_image10.png)

-   We can apply the base.html template to all flatpages at once by modifying
    the default.html file in our templates/flatpages folder. Just add one line
    to specify that it extends base.html as follows:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends 'base.html' %}
{% block content %}
   <h2>{{ flatpage.title }}</h2>
   {{ flatpage.content }}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Now the About Page and any other flat page that we create will be styled
    using the same look and feel as the rest of the site.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/we_are_social2.png)

-   Edit base.html to make the About link point to the About page:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<ul class="nav nav-pills pull-right">
    <li><a href="/">Home</a></li>
    <li><a href="/pages/about/">About</a></li>
    <li><a href="#">Contact</a></li>
</ul>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
