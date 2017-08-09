Template Inheritance
====================

### TEMPLATE INHERITANCE

One of the most common problems in web development is that of how to reduce the
duplication and redundancy of common page areas, such as site-wide navigation.

Django provides a means to extend a base “skeleton” template file. We can define
our site-wide components once and then inherit from that file, adding in the
aspects of the site that do change into child templates. The base template
contains all the common elements of your site and defines blocks that child
templates can override.

1.  Modify your **base.html** to include the following code:  
      
      
    

    ![template-inheritance-base-html.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124952_image9.png)

      
      
    

In our example, we have created a block element that will be populated with data
from a child template. Within the opening tag – **{% block page_content %}** –
“page_content” is an arbitrary identifier for the block and can be changed to
suit your preference and expected content.

The closing tag – **{% endblock %}** – is used to indicate the end of the block
scope.

1.  Now let’s create child template.

    Create and save a new file called **home.html** to the template/HelloWorld
    directory and add the following content to the file:  
      
      
    

    ![template-inheritance-home-html.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124952_image10.png)

      
      
    

The first line of the child template contains a tag with a reference to the
parent template. Notice the use of the **extends** keyword to create the
inheritance relationship.

The child template also has a block with a matching name to the parent template.
Inside the block we have two variables. As we did in the earlier walkthrough
example, we will bind data to these variables from  a view. Let’s do that now.

1.  Add a function
    called **inheritance_test** to **views.py** in **HelloWorld_app**.

By the way, we would normally only have one or two functions in a view that
reflected the purpose of the app. We’ve left the other functions (views) in here
as a learning exercise to compare and contrast the syntax and purpose of each.

Your code should look like below:  
  
  


![template-inheritance-view.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124952_image11.png)

  
  
  
Don’t forget to add a url mapping to the view in **urls.py**, and give the url a
name.  
  
  


![template-inheritance-url.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124952_image12.png)

  
  


1.  Run your web server and test your code.  
      
      
    

    ![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124952_image13.png)

      
      
    

  
  


### SUMMARY

In this lesson, we’ve learned that:

-   Templates are used to separate the presentation of a document from its data
    and logic.

-   A template defines placeholders and logic through the use of template tags
    and variables that determine how the document is rendered.

-   We can define site-wide components once in template file and then inherit
    from that file, adding in the aspects of the site that do change into child
    templates.
