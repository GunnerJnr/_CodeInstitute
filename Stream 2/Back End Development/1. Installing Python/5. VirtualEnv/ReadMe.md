Lesson Walk Through 
====================

 

### VIRTUALENV

Virtualenv is slightly different to simplejson in that it’s not designed to be
imported into your programs. Instead, it’s supposed to be used from the command
line.

1.  Using the command line, navigate to your home folder, i.e. `%USERPROFILE%`
    or `$HOME`

2.  Install virtualenv

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-13.1.2-py2.py3-none-any.whl (1.7MB)
    100% |################################| 1.7MB 2.4MB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-13.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Note that nn Mac or Linux, you’ll need to use sudo: `sudo pip install
    virtualenv`

2.  Our environments are just directories, so we need to create a directory to
    keep them all in. Create the directory virtualenv and cd into it:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>mkdir virtualenv
C:\Users\will>cd virtualenv
 
C:\Users\will\virtualenv>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Now create an environment called ‘test’ by using the virtualenv command.
    It’s going to create a folder called ‘test’ with our environment in it:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will\virtualenv>virtualenv test
PYTHONHOME is set.  You *must* activate the virtualenv before using it
New python executable in test\Scripts\python.exe
Installing setuptools, pip, wheel...done.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  We haven’t activated it yet, since we’re still inside our global Python
    environment. Activate it now by running activate.bat inside the Scripts
    folder in our new environment:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will\virtualenv>test\Scripts\activate
(test) C:\Users\will\virtualenv>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.   For Linux and Mac, use the following instead:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
. test/bin/activate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  You will notice that your prompt has changed and now includes the name of
    the virtual environment you’re in. We can check that we have a nice, new,
    clean environment by using pip list:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(test) C:\Users\will\virtualenv>pip list
pip (7.1.2)
setuptools (18.2)
wheel (0.24.0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can see that `simplejson` doesn’t appear in the list.

 

1.  We can switch back to the global environment by deactivating this
    `virtualenv` using the deactivate command. Our prompt returns to normal and
    we can see by using pip list that `simplejson` is back:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(test) C:\Users\will\virtualenv>deactivate
C:\Users\will\virtualenv>pip list
pip (7.1.2)
setuptools (16.0)
simplejson (3.8.0)
virtualenv (13.1.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

You can find more information about `virtualenv`
at <https://virtualenv.pypa.io/en/latest/>. You might also want to check out the
module virtualenvwrapper, which makes it slightly easier to use.

 

### SUMMARY

In this lesson, you have:

-   Installed Python and learned how to use the command line.

-   Been introduced to the package manager and installed a package.

-   Learned about virtualenv and creating isolated environments.

-   Used IDLE to create, save, and run a program.

 

Challenge
=========

 

-   Use pip uninstall to uninstall `simplejson`, and pip list to make sure it is
    gone.

-   Using the command line, try to make some new folders.

-   Make a new virtual environment, activate it, and try installing a module.
