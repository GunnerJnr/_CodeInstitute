### ADDING IMAGES TO A POST

We’ll start with the images. As in the last two lessons, we’ll first modify
our **Post** model.

To do this:

1.  Add a new **imageField** to the **Post** model.

2.  Install **Pillow** to handle image storage and retrieval.

3.  Migrate.

4.  Add **MEDIA_ROOT** value to **settings.py**.

5.  Add a custom url pattern to the project level **urls.py** file.

6.  Add a reference to the **Post** model image attribute in an **\<img\>** tag
    inside the **postdetail**template to view.    
    

### ADD A NEW IMAGEFIELD TO THE POST MODEL

1.  Let’s add an image attribute and related table field.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#author is linked to a logged in user in the "auth_user" table
   author = models.ForeignKey('auth.User')
 
   title = models.CharField(max_length=200)
   content = models.TextField()
   created_date = models.DateTimeField(default=timezone.now)
   published_date = models.DateTimeField(blank=True, null=True)
   views = models.IntegerField(default=0) # Record how often a post is seen
   tag = models.CharField(max_length=100, blank=True, null=True)
 
   image = models.ImageField(upload_to="images", blank=True, null=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice that we specify the **upload_to** directory called **image** for our blog
post images. This directory will live inside a media directory that we’ll
specify in step 4.

 

### NOTE

This is the point where we would normally run our **makemigrations** and
migrate commands to update the database schema. But in this instance, we can’t
do that just yet.

 

-   We need Python’s pillow imaging library in place first, so
    that **ImageField** can be used. Use **pip** to install **pillow**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 pip install pillow==2.9.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Now run the **makemigrations** and **migrate** commands and you’ll see the
    image field added to the table. As a reminder, notice how the migrate
    command brilliantly preserves our existing row data while adding the new
    field.

A few steps further down the line, we’ll see that new image table field only
stores the relative path to where the image lives, and not the image itself.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image1.png)

 

-   Next, we need to tell Django where to find our image files. For security
    reasons, we separate our images from our other static content. We’ll update
    our settings file to let Django know where to place and locate images.

    Add the code below to **settings.py**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From now on when we add images to our project, they will be stored in the media
directory. But in particular, our blog posts will be stored in a sub-directory
of media called **images** that we specified in our **ImageField** function in
Step 1.

-   Because images and other media in HTML are displayed using a URL specified
    in the src attribute, Django uses the url mapping pattern to find them. To
    do that, we set up a url pattern in our project level **urls.py** file.
    Import the **MEDIA_ROOT** setting as shown on **line 4**below. Then map a
    url to the **MEDIA_ROOT** folder as shown on **line 14**. That way, when a
    post is displayed with an image, Django knows the path to the media
    directory location.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
 
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_prj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Next, we modify our **postdetails.html** file to display an image at the top
    of our post content.  For good UX, we’ll only render the **\<img\>** tag if
    there is an an image entry path stored in the table for that post. Wrap the
    image tag in an Django template language **if-statement**and prefix the
    reference to **post.image** with a reference to the **/media/** directory.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
<div class="row">
   <div class="col-xs-9">
      {% if post.image %}
          <img src="/media/{{ post.image}}">
      {% endif %}
      <p>{{ post.content|linebreaks }}</p>
      <p><button class="btn btn-default" 
onclick="location.href='/blog'">Back to Blog</button> </p>
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   We’ll test our changes by firing up the server and going to the admin page.
    Once logged in, select an existing post and open it for editing. We can see
    that there is a new **Choose File**upload button in place to upload a post
    image. Click this button and select an image for your post.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image2.png)

-   Save your changes and open the main blog view. Select the post you added the
    image to and click the “**Read More**” button to view your blog image.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/12/1449749030_image3.png)

  
  

