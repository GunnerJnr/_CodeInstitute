### CATEGORISE THE POSTS USING TAGS

Let’s group our posts into some kind of categories. This is handy when looking
for particular topics, trends, or general areas of discussion.

1.  Just like we did when adding a counter for the post views, we’ll start by
    updating our **Posts**model. In this case, we’ll add a tag attribute and
    table field.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
    # author is linked to a logged in user in the "auth_user" table
    author = models.ForeignKey('auth.User')
 
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Update the Posts database table by
    running **makemigrations** and **migrate**.

2.  Update the **blogposts** and **postdetail** templates to include the tag.
    We’ll place the tag to the right of the view count. Let’s add
    some **\<strong\>** tags around the views and tag labels to make them stand
    out from their values.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{{ post.published_date }} | <strong>Views</strong> {{ post.views }} | <strong>Tag</strong> {{ post.tag }}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Fire up the web server and log in to the admin page. When you are in, open
    one of the blog posts you created. You’ll see a new textfield with the “tag”
    label, where you can add a tag to your post. Pop some text into it.  
    

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1453160720_image3.png)

1.  Save your changes and find the blog post you updated on the blog post list.
    You should see the tag value right beside the views count. The same should
    be seen in the blog detail view.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1453160720_image4.png)
