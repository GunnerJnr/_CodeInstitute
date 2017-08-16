Creating a Template
===================

##### In this unit the students will learn how to build a template using Django

### CREATING A TEMPLATE

So let’s refactor our code and move the content into a template.

1.  Create a new directory called **templates** in
    our **HelloWorld_app** directory

2.  Create a new directory called **HelloWorld** in the templates directory

The structure should now look like below:

![pycharm-added-templates-dir.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image3.png)

1.  Create a new file called **base.html** inside the HelloWorld directory by
    right-clicking on the HelloWorld directory and hovering over New and
    selecting HTML File and call it **base.html**

So our structure now looks like this:

![pycharm-added-base-html.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image4.png)

1.  Add the following code to **base.html**:

    ![pycharm-edit-base-html.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image5.png)

   
A template contains variables, which get replaced with values when the template
is evaluated, and tags, which control the logic of the template.

Embedded amongst some standard HTML in our template is a template variable
denoted by the double braces enclosing the variable name – **{{ current_date}}**

Variable names consist of any combination of alphanumeric characters and the
underscore (“**\_**“).

The dot (“**.**“) is also used – **{{ some_object.some_attribute}}**

Django enables us to assign a value to a variable of the same name in a view,
and then inject the value into the matching variable in the template.

5. Create a view linked to the template (note that PyCharm might try tell you
that there’s no module named **datetime**. However, Django should resolve this
so we can ignore it).

![pycharm-add-new-view.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image6.png)

6. Create a URL mapping to the view.

![pycjarm-url-for-now.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image7.png)

7. Run your web server and test.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455124056_image8.png)
