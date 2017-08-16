### CREATE A NEW CHILD TEMPLATE

1.  Update the **blogposts.html** template to use the new styles created in the
    last lesson.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
 
{% block content %}
    {% for post in posts %}
        <div class="row">
            <hr>
            <div class="col-md-2 col-sm-3 text-center">
                <a class="story-img" href="#">
                    <img src="http://placehold.it/100" style="width:100px; height: 100px; background-color: #12ABB2; color: #ffffff;" class="img-circle">
                </a>
            </div>
            <div class="col-md-10 col-sm-9">
                <h3>{{ post.title }}</h3>
                <div class="row">
                    <div class="col-xs-9">
                        <p>{{ post.content }}</p>
                        <p><button class="btn btn-default">Read More</button></p>
                        <p>{{ post.published_date }}</p>
                    </div>
                </div>
            </div>
        </div>
    {% endfor %}
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Create a templates folder in the blog app (as opposed to the root level
    template folder currently used).

2.  Move the **blogposts.html** file from the root level templates folder to the
    blog app templates folder.

3.  Run the server and note that it continues to work with
    the **blogposts.html** template in its new location.

4.  Create a new template file called **postdetail.html** and save it to the
    blog app templates folder (the same location as
    our **blogposts.html** file).

5.  Put the same content from **blogposts.html** into the
    new **postdetail.html** file.

6.  The **postdetail.html** template will show one post, not a list. So
    remove **{% for post in posts %}** and  
    **{% endfor %}**

7.  Remove the **\<hr\>**

8.  In **postdetail.html** modify the caption of the **‘Read More’** button so
    that it is **‘Back To Blog’**

So, the new child template is ready to go. Now we’ve got to figure out how to:

-   Link to it from a list of posts

-   Link back to the post list
