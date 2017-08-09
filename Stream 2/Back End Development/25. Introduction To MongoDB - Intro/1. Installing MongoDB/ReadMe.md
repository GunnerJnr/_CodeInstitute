### WHAT IS MONGO DB?

[MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) is a
document [database](http://lms.codeinstitute.net/glossary/database/).
A [record](http://lms.codeinstitute.net/glossary/record/) in [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) is
treated as a document, which is a data structure made up
of [field](http://lms.codeinstitute.net/glossary/field/) and value
pairs. [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) documents are
similar to JSON objects. The values of fields may include other documents,
arrays, and arrays of documents.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image2.png)

The [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) [database](http://lms.codeinstitute.net/glossary/database/) consists
of a set of databases in which
each [database](http://lms.codeinstitute.net/glossary/database/) contains
multiple
collections. [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) is
schema-less, which means that every collection can contain different types of
objects. Every object is also called document, which is represented as a [JSON
(JavaScript Object
Notation)](http://lms.codeinstitute.net/glossary/javascript-object-notation-json/) structure:
a list of key-value pairs. The value can be of three types: a primitive value,
an array of documents, or again a list of key-value pairs.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image3.png)

Let’s see how a RDBMS
and [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) differ:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image4.png)

### DOWNLOADING MONGODB

1.  Go to the the[  MongoDB downloads
    page](https://www.mongodb.org/downloads#production). 

2.  Choose any version compatible with your operating system.

3.  Install.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image5.png)

### INSTALLING AND RUNNING MONGODB ON WINDOWS

Click on the msi installer to get set up. You’ll find that the software has been
added to **c:\\program
files\\**[MongoDB](http://lms.codeinstitute.net/glossary/mongodb/)

[MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) contains only 18 files
in the bin folder. This is an impressively light footprint compared to the more
traditional [RDBMS’](https://en.wikipedia.org/wiki/Relational_database_management_system) that
hog both disk space and memory.

   
It’s recommended to
add **\$**[MongoDB](http://lms.codeinstitute.net/glossary/mongodb/)**/bin** to
Windows environment variable, so that you can access
the [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/)’s commands in
command prompt easily.  
To set variables in Windows 8 and Windows 10:  
From the Desktop, right-click the very bottom left corner of the screen to get
the Power User Task Menu.  
From the Power User Task Menu, click System.  
Click the Advanced System Settings link in the left column.  
In the System Properties window, click on the Advanced tab, then click the
Environment Variables button near the bottom of that tab.  
To create a new environment variable, click New and set the variable name to
\$[MongoDB](http://lms.codeinstitute.net/glossary/mongodb/)\\bin and variable
value to the correct directory root for your machine.

![Environment Variable](http://codeinstitute.wpengine.com/wp-content/uploads/2016/09/EnvVar.png)

### SET UP OUR ENVIRONMENT

The command we will use most often is **mongod.exe**. This command runs an
instance of [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) on a local
server and allows access to your data.  

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image6.png)

**mongod.exe** requires some config parameters passed to it in order to get
things up and running.

We can pass in the config parameters using two ways:

-   Using command line options or

-   Using a configuration file

### USING THE COMMAND LINE OPTION

There are a number of parameter options that we can pass in, but for the purpose
of getting up and running we’ll take a look the essentials:

**–dbpath \<path\>**: the path to the directory where we store our data files.
If you don’t specify this, then the server won’t run because it won’t know where
to access data. Let’s create directory.

**–logpath \<log-file-path\>**: the location used to to store the process log
files, including startup/shutdown data.

**–port \<port\>**: port number that mongod used to listen for connection
requests from clients. The port defaults to 27017 if not specified.

Before we open up the command line, let’s create a data directory to provide a
path for –dbpath.

-   c:\\mongodata\\data will work just fine.

Let’s fire up the server and test our install.

1.  Open up an instance of the command prompt.

2.   Navigate to
    the [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) bin directory
    to get to the** mongod** command. This directory root may differ for you
    depending on where
    your [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) has been
    installed. The mongod.exe program exists in the bin directory so this is
    where you need to type in a mongod command.

3.  Enter the command below to set up your server:

4.  Once you hit enter, you should see that the server is outputting log info to
    the console.

5.  It’s always good practice to save log information rather than losing it
    every time we close down the command line window, so let’s do that now.
     Enter **ctrl+c** to shut down the server.

6.  Add a new subdirectory to  **c:\\mongodata** called **logs.**

7.  Add a log location and filename parameter to our startup command, as shown
    below:  

8.   Hit enter to run the server again and you should see that the log entries
    are no redirected to that file rather than the console (but the server
    process will still keep running until shut down).

9.  Go to your newly created logs directory and take a look inside, you’ll see a
    file called **logs**. Open it using notepad and you’ll see the log entries.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image12.png)

1.  Enter **ctrl+c** to shutdown the server, then hit the up arrow key to return
    to the last command and run again.

2.   Shut down the server again and this time run the command with a new
    parameter added called   
    **–logappend**. Your log entries will now append to the logs file.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image14.png)

### CREATE A CONFIGURATION FILE

We can make life even easier for ourselves by creating a configuration file that
holds most of the startup parameters for us. That way, instead of typing out all
the parameters each time we start the server, we just refer to the configuration
file. The configuration file contains the parameters in key=value form and each
one is specified on its own
line. [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) has the smarts
to look inside that file to find out what it needs to do to get up and running.
 

1.  Add a new subdirectory to **c:\\mongodata** called **config**.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image15.png)

1.   Create a new file in the config directory called **mongoConfig.conf**

2.  Add the following text to set up the config file. Each parameter is listed
    on its own line. Then save your file.

 

\#Mongo db config settings  
   
dbpath=c:\\mongodata\\data \# databases location  
port = 27017 \# default port  
bind_ip = 127.0.0.1 \# default ip  
logpath = c:\\mongodata\\logs\\mongo \# log file location  
logappend = true \# append to master log file

1.  Run the command below to test your configuration file. This time we need
    only to tell **mongod** where to find the config file. If it works, your log
    file should be updated with the server startup timestamp and related server
    session log information.

mongod --config C:\\mongodata\\config\\mongoConfig.conf

![](http://codeinstitute.wpengine.com/wp-content/uploads/2015/11/1448201978_image16.png)

###  

Now we are ready to play with some data.
