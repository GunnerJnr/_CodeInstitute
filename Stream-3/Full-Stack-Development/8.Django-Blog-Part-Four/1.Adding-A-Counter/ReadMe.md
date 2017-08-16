### ADDING A COUNTER – UPDATE THE POST MODEL

We’ll start by recording the number of times a blog post has been viewed. Each
time a user views an individual blog post, we’ll record that in our database
table. And to do that, we’ll first update our **Post** model. Add the code shown
on **line 8** below. This creates a new views table field that has an initial
value of 0.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Once we’ve updated the model, we need to remember to update the database. Run
the **migrations** command in the command line within our project root:

1.  python manage.py makemigrations

2.  python manage.py migrate

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1453160720_image1.png)

 

### UPDATE THE VIEW

Every time an individual post is read, the **post_detail** view is called. So
that’s where we need to place our counter. We’ll read back the value in
current **views** attribute value and clock it up by one. We’ll then update the
table with the incremented value before passing the model instance down to the
template.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def post_detail(request, id):
    post  = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the number of post views
    post.save()
    return render(request, "postdetail.html",{'post': post})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### UPDATE THE TEMPLATE

Now let’s update both child templates to display the number of views each post
has had.

The same code will be inserted in both **blogposts** and **postdetail**. We’ll
put the views count beside the published date at the bottom of a blog post.
Separate the published date from the views count with a  pipe “**\|**“.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<p>{{ post.published_date }} | Views {{ post.views }}</p>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fire up the server and test.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1453160720_image2.png)

 

Nicely done!
