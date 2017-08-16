### LINK TO THE POST DETAIL

When we click the “Read More” button below a post entry, we want Django to take
us to the post detail. How can we achieve this?

We’ll use the `primary key ID` assigned to the post entry in our database as our
post identifier.

We’ll send the `ID` to the `detail` template as part of the
button’s `onclick` event and use JavaScript’s `location.href` to redirect us.

We then need to modify our `urls.py` file to:

-   recognise the `ID` passed over when the button was clicked

-   invoke a newly created function in `views.py` called `post_detail` that will
    take the post `ID` as a parameter.

The `post_detail` function (view) will then:

-   use the `ID` to invoke the model and return the post details

-   pass the result to the new detail template.

Let’s start wiring the whole thing together!

In `blogposts.html`, add an inline `onclick` event handler to our “Read More”
button.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="col-xs-9">
    <p>{{ post.content }}</p>
    <p><button class="btn btn-default" onclick="location.href={{ post.id }}">Read More</button></p>
    <p>{{ post.published_date }}</p>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We pass the `post.id` as the value to our href when the button is clicked.
The `urls.py` will sent that `ID` as a url pattern and try and deal with it. So
we need to set things up so `urls.py` will know what to do. Right now, it will
fail.

-   Fire up the server and test it. Enter `http://localhost:8000/blog` to load
    the posts.

-   Click on the “Read More” button for a post. Look at the url passed in.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449668568_image1.png)

 

### CREATE A REGULAR EXPRESSION

We need a regular expression that can recognise the post **ID** being passed in.
One way to do this would be to create a url for each post id passed in, but this
would be hugely inefficient and unmaintainable.

Add the url pattern shown below to our **urls.py** file created at the app
level.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s going on here? – **`r’^blog/(?P<id>\d+)`

`r’^blog/`

-   There’s nothing really new in this part of the url pattern. It just means
    look for a url that begins with **“**`blog/`**”** in the text.

`(?P<id>\d+)`

`?P<id>` This is the new bit;  It means that Django will take a value that you
pass in the url and transfer it to a view as a variable called `id`.

`\d+` is a digit (a character in the range 0-9), and **+** means the digit is
allowed to occur 1 or more times. If a character other than a digit is passed
in, then it will be ignored.

-   `http://localhost:8000/blog/2345/` will work

-   `http://localhost:8000/blog/hello/` will fail.

`()`

-   The round brackets group the regular expression together

`/$`

-   just means the end of the pattern

### CREATE THE VIEW

We now need a view capable of taking the `ID` as a parameter passed in from the
url dispatcher, and using that ID to fetch our model and bind it to
the `postdetail.html `template.

Go to `views.py` in our app and create a new view called `post_detail`. It
should look like below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
...
 
...
def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=id)
    return render(request, "postdetail.html", {'post': post})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What’s new here?**

**Line 1** – We have an additional import; `get_object_or_404`

-   We will use this to gracefully fail if there is no object returned, i.e., if
    we look for a record that doesn’t exist, a rudimentary 404 page not found
    message will be displayed. This 404 page can be fully customised and we’ll
    indeed do that in a later lesson.

**Line 5** –  Our function has a second parameter which takes the `ID` passed
from the url dispatcher and uses it to locate the primary key in the table.

**Line 13** – We use the `get_object_or_404` function, passing in
the `Post` model and the id primary key. If successful, a single blog post
object is returned and assigned to the post variable.

**Line 14** –  We pass the single post entry to our postdetail template . This
is why we don’t need a `for-loop` in this template.
