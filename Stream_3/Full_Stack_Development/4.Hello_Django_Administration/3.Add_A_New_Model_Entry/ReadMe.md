### ADD A NEW MODEL ENTRY

As promised in the previous lesson, there’s a hassle-free way of adding model
data via the admin that removes the need to use the Python shell. We’ve just
seen how easy it is to wire up our models to the admin, then edit an entry. It’s
just as easy to add a new model entry.

1.  Select **ModelTest_app** in the breadcrumbs link (home is fine too) to take
    us to the **Contact**model.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image14.png)

  
  


1.  Click on the **Add** link and you will be presented with three fields
    mapping to our model attributes. Notice that the id primary key is not
    visible, because that is created automatically by default.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image15.png)

  
  


1.  Fill in the fields to add a new contact then hit **Save**, or “Save and add
    another” if you want to add more contacts.

  
  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449490658_image16.png)

  
  
  
4. Try and create a new contact with first and last names greater than 255
characters, or a mobile number longer than 20 characters. You’ll find that you
are unable to; the text input length is governed by the table field constraints.
