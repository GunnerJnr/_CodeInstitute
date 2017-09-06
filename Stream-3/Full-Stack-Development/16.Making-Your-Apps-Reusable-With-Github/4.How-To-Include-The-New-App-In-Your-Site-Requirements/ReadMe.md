How to Include the New App in Your Site Requirements
====================================================

##### In this unit the students will learn how to add their reuseable Django app to their requirements.txt file

 

### HOW TO INCLUDE THE NEW APP IN YOUR SITE REQUIREMENTS

We’ve now come to the exciting part! We need to upload this to GitHub, so let’s
get it on the interwebs!

Login to your GitHub and create a new repository:  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452278888_image5.png)

 

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452278888_image6.png)

  
Fill in the details required and click *Create repository* to complete the
process.

After creating a new repository on GitHub, we need to start the repo in
our `reusable_blog_app` folder:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git init
git remote add origin https://github.com/<your github username here>/reusable-blog-app.git
git add .
git commit -m "initial commit"
git push
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our new reusable blog is now online and ready to be included!

### USING THE REUSABLE_BLOG

Let’s open up our we_are_social project in Pycharm and we’ll see how to use this
app in a Django project.

If at any point you run into any issues with your code, you can return to this
starting point by following these steps:

In the terminal run the following commands:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/Code-Institute-Org/we_are_social.git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd we_are_social
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git checkout paypal_subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you have a virtualenv setup in Pycharm. You’ll have to update the
requirements.txt file, adding a git link such as `git+https://github.com/<YOUR
GITHUB USERNAME>/reusable_blog_app.git` with your GitHub username (and changing
the repo name if you used something else than reusable_blog_app\>. Once that’s
done, you can go ahead and run `pip install -r requirements.txt` to install the
dependencies.

Run `python manage.py migrate`

### SUMMARY

As you can see, packaging your apps in this way can allow you to compose sites
quickly and easily with existing apps.

Packaging apps may vastly increase your development speed and greatly reduce the
time a customer has to wait for development. This is one of the most powerful
reasons why Django is so widely used around the world.
