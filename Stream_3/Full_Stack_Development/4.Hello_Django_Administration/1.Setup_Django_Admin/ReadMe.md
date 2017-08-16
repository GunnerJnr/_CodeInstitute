### SET UP DJANGO ADMIN

So how do we go about using the admin module?

Luckily, Django’s admin module comes already listed in
the **INSTALLED_APPS** table in your project settings file.  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image1.png)

  
  
  
Just as handy is the fact that the URL file for apps already has a url mapping
to the admin page.  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image2.png)

  
  
  
Once an app has been registered with our project, we can fire up our test web
server and view the admin (localhost:8000/admin). Very nice indeed.  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image3.png)

  
  
  
We then need to create an admin user (superuser) in order to log in to the admin
screen.  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image4.png)

  
  
  
Use the newly created username and password to enter the admin screen.

  Note: If this were a brand new project, we would first run the migrate command
to set up our admin tables in our SQLite database.

  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image5.png)

  
  
  
And we’re in!  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image6.png)

  
  
  
We can see that we have the means to administer users and groups right out of
the box. Explore the interfaces and add some users and groups. We’ll get into
this in more detail in a later lesson; our current goal is to add new contacts
to our database.

So let’s get our models talking to our admin.
