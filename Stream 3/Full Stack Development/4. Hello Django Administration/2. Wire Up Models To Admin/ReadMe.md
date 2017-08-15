### WIRE UP MODELS TO ADMIN

We link our admin to our models within the **admin.py** file in our app.

1.  Import the Contact model.

2.  Register the model with the site (project).

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image7.png)

  
  


1.  Refresh your admin screen.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image8.png)

  
  
  
And there it is!  A Contacts section where you can edit existing contacts or add
new ones.   
  
  
Let’s modify one of our existing contacts first:

1.  Click on the **Edit** icon and you’ll see a list of contacts in our
    database.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image9.png)

  
  
  
The contact full name is shown. Remember that we added a  **\_\_ str_\_** method
to display the joined **first_name** and **last_name**.

1.  Select one of the entries for editing.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image10.png)

  
  


1.  Edit one of the fields and click **Save**.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image11.png)

  
  


1.  We return to the **Summary** screen. A message is displayed to confirm that
    the update was successful.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image12.png)

  
  
  
We can also check the change history for the record. This is really useful for
tracking any intended or unintended changes to your models.

Click on the contact you edited, and then click on the **History** link in the
top right-hand corner of your screen to view the history. You should see
something like below:  
  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image13.png)
