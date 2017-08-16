No Challenge 
=============

 

This lesson did not contain a challenge. It did however contain a small walk
through. I have taken the liberty of adding the walk through file to the folder
‘lesson solution’. I will now list the steps taken below.

 

### MANAGING PACKAGES WITH PIP

One of Python’s greatest features is its extensive standard library, i.e., the
modules which are installed alongside Python. It includes many modules for
common functions, but sometimes there are third party modules which it doesn’t
make sense to include in the standard library. A gaming library, for instance,
might be too specialised.

For these situations, Python includes a tool called pip, which can install
modules that other people have created. While pip can install packages from
other locations, it is mainly used to install packages from
pypi (<https://pypi.python.org/pypi>), otherwise known as ‘the cheese shop’,
which is a reference to a famous Monty Python sketch.

Although it is outside the scope of this course, anyone can create a module for
other people to use – it’s just a case of uploading your program to pypi in a
particular format. See<https://wiki.python.org/moin/CheeseShopTutorial> for more
information about this.

We’re going to install and use simplejson, a small library for reading and
writing JSON files and strings. Using the command line again, let’s first see
what packages we have installed and their version using pip list. It doesn’t
matter which directory you’re currently in.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>pip list
pip (7.0.1)
setuptools (16.0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the two modules installed by default with Python, one of which is pip,
and the other doesn’t concern us right now.

So let’s search for simplejson to see if it actually exists:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>pip search simplejson
exemelopy   - exemelopy is a tool for building XML from native Python
              data-types, similiar to the json/simplejson modules
simple_json - Compatibility shim for simplejson
omnijson    - Wraps the best JSON installed, falling back on an
              internal simplejson.
simplejson  - Simple, fast, extensible JSON encoder/decoder for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It does exist, and a few other modules which mention it are also listed. So
let’s install it. If you don’t supply a version number, it just installs the
latest version, which is usually what you want.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>pip install simplejson
Collecting simplejson
  Downloading simplejson-3.8.0.tar.gz (75kB)
    100% |################################| 77kB 772kB/s
Installing collected packages: simplejson
  Running setup.py install for simplejson
Successfully installed simplejson-3.8.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now when we do ‘pip list’, simplejson is shown as being installed:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Users\will>pip list
pip (7.0.1)
setuptools (16.0)
simplejson (3.8.0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now create a new file in IDLE, paste in the following code, save it, and run it:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import simplejson
 
raw_json = """
[
   "foo",
   {
       "bar": ["baz", null, 1.0, 2]
   }
]
"""
 
decoded_json = simplejson.loads(raw_json)
print decoded_json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At **Line 1**, we import the module we just installed. At lines 3-10, we define
a multiline string with some JSON, which you should be familiar with.

At **Line 12**, we use the imported module to decode the json to a normal Python
list.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
[u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can play around with this list; for instance, just print the first item:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> decoded_json[0]
u'foo'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We’ve installed a module, but there’s a problem. This module was installed
globally, so every Python program that you write will now have simplejson
available to it. This doesn’t seem like a problem initially, but what if in a
year’s time you write a program and want to use the very latest version of
simplejson? You will update simplejson, so now both your programs will be using
the new version – but the older one was written for the older version of
simplejson, so it now might not work.

This what is known as Dependency Hell
(<https://en.wikipedia.org/wiki/Dependency_hell>), which is worth having a read
of. The solution to this is for each of our programs to have its own
self-contained environment with its own set of modules, which no other program
can touch.

For this we can use a module called `virtualenv`.
