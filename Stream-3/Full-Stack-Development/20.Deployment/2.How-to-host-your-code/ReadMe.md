How to Host Your Code
=====================

##### In this unit the students will learn how to host their Django project on Heroku

### HOW TO HOST YOUR CODE

Let’s head over to <https://dashboard.heroku.com/apps> so we can create a new
app. In order to do this, we’ll click on the plus symbol over in the top right
hand corner and click on **Create new app**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image1.png)

  
Next we’ll be presented with a new page. You can choose to give your app a name
if you wish. This will mean that your app will be hosted at **\<app
name\>.herokuapp.com**. For this reason the app names need to be unique. You can
also select the **Runtime**. Choose the region nearest to you.

For this example, let’s create a new app
called **code-institute-social-staging**. Let’s also set the **Runtime
Selection** to Europe.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image2.png)

  
Once you’ve selected a new name and Runtime region, go ahead and click
on **Create App**.

   
Now that we have our app set up, we need to update
our **SITE_URL**, **ALLOWED_HOSTS** and **PAYPAL_NOTIFY_URL** to include the
new **\<your-heroku-app\>.herokuapp.com** domain (make sure that you only
include the host name and not http, nor any other characters).

This will bring us the dashboard for our new app. Once we’re here, we can go
ahead and open up our project in Pycharm.

As with the Flask app that we deployed to Heroku in Stream 2, we’ll need to
use **gunicorn** to run application on Heroku. We’ll also need to add a
Procfile and create a Procfile.local so we can test Heroku locally.

Firstly, let’s go ahead and add **gunicorn** to the **requirements/base.txt**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
gunicorn==19.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you’re using Mac OS X or a Linux based operating system, you’ll need to
install gunicorn now. You can do that by running the following command from your
project’s root directory:

`pip install -r requirements/dev.txt`

This will ensure that all of the development dependencies are installed,
including gunicorn.

Next, let’s go create our Procfile. Right-click on
the **we_are_social** directory in Pycharm and add a new file
called **Procfile**:

`web: gunicorn we_are_social.wsgi:application`

Here we’ll be using Django’s **wsgi.py** file for our server.

Right-click on the **we_are_social** directory in Pycharm and add a new file
called **runtime.txt**. In this file add the following line of code which will
tell Heroku that you are using Python 2.

`python-2.7.12`

**Mac OS X/Linux:**

Next we’ll create our **Procfile.local**. This is what it should look like for
Mac OS X or Linux:

`web: gunicorn we_are_social.wsgi:application`

Then we need to set the Django environment that we’ll be using locally. This is
done by simply running this command from the command line:

`export DJANGO_SETTINGS_MODULE=settings.dev`

**Windows:**

Next we’ll create our **Procfile.local**. This what it should look like for
Windows:

`web: python manage.py runserver`

Then we need to set the Django environment that we’ll be using locally. This is
done by simply running this command from the command line:

`set DJANGO_SETTINGS_MODULE=settings.dev`

Now that we have that done, we can go ahead and run the following command from
the Pycharm terminal:

`heroku local -f Procfile.local`

And now we should be able to see our app in the browser when we go
to **localhost:8000**.

   
After these changes have been made, they will need to be pushed into the GitHub
repository.

Now that we’ve made all the changes needed to get Heroku up and running, we’re
going to connect Heroku to our Github account. Open
up **https://dashboard.heroku.com/apps/\<your-app-name\>/deploy** and under
the **Deployment method** heading, click on **GitHub**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image3.png)

  
Once we’ve done that, we’ll be sent to GitHub in order to grant Heroku access.
Go ahead and grant Heroku access by clicking the **Authorize** application.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image4.png)

  
You may not see the Organization access section unless you’re part of an
organization, so you can ignore that section.

Once that’s done, you’ll be able to select the repository that you want to share
with Heroku.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image5.png)

  
Next thing we’ll do is go to the **Automatic deploy** heading. What we want to
achieve here is to tell Heroku to watch out for any changes that occur on the
master branch of our GitHub repository and deploy the latest code. In order to
this, we select **master** from the drop down menu.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/04/1460456931_image6.png)

  
Once that’s done, go ahead and click **Enable Automatic Deploys**.

The last thing that we need to do is start our web worker. To do this, first
run:

heroku login

Next we’ll need to set our environment on Heroku by running the following
(replacing YOUR_HEROKU_APP with the name of your Heroku APP):

`heroku config:set DJANGO_SETTINGS_MODULE=settings.staging --app
YOUR_HEROKU_APP`

This will just update the Heroku configuration that Django will read from.

We’ll also need to run the following:

`heroku config:set DISABLE_COLLECTSTATIC=1 --app YOUR_HEROKU_APP`

We need to this because Django will attempt to load all the static files from
our own static directory, as well the static files from other sources, such as
the admin panel, or Bootstrap forms. We don’t have it set up yet, so the above
command will disable the static collection.

Next, run:

`heroku ps:scale web=1 --app YOUR_HEROKU_APP`

After that you should be able to see the project open in a new browser tab after
you run:

`heroku open --app YOUR_HEROKU_APP`
