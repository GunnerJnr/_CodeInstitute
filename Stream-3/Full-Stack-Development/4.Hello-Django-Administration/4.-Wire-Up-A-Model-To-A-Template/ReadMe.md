### WIRE A MODEL TO A TEMPLATE

Let’s display our contact list on a template:

1.  Create a templates directory in **ModelTest_app**.

2.  Create a **ModelTest** subdirectory in templates.

3.  Create a template file called **home.html** and save it to
    the **ModelTest** directory.

4.  Add valid HTML document markup, including head and body elements.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image17.png)

  
  


1.  Add a template language block within the body tags.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image18.png)

  
  


1.  Create a view that maps to the template. The view should look similar to
    this:

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image19.png)

  
  


-   We import the **Contact** model.

-   Also notice here that we are using **Contact.objects.all()** to get all of
    the contact entries from the database.

-   We are sending the list to the **home.html** template via
    the **contact_list** variable.

1.  In order to display the contacts we need some kind of loop. And, as you
    might imagine, the Django template language provides us with
    a **for-loop** to do this.  

2.  Modify your template to look like below:

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image20.png)

  
  
  
As the loop iterates through the contents of **contact_list**, it assigns the
current **Contact** object in the list to the **contact** variable. This
variable will then be used to display the Contact details.

1.  Access and display the details of each contact.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image21.png)

  
  


1.  Link the view to your project **urls.py**

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image22.png)

  
  


1.  Fire up your web server and test the data in a browser.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image23.png)

  
  


1.  Not the most fabulous-looking presentation, is it? Let’s dress the template
    up a bit.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image24.png)

  
  


1.  Refresh your browser to see the changes.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image25.png)

  
  
  
Still not exactly award winning UX, but it’s functional. We’ll start adding eye
candy to our work in later lessons, but for now it’s all about getting to grips
with the mechanics of the framework.  
  
  


### SUMMARY

  
In this lesson, we’ve learned that:

-   We can administer model data through a built-in administration module

-   Django’s admin module comes already listed in the **INSTALLED_APPS** table
    in the project settings file

-   We link our admin to the models within the **admin.py** file in our app

-   We can check a record’s change history using the History link

-   Django provides a **for-loop** to display contacts
