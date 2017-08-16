No Challenge
============

 

This lesson had no challenge so to speak. It did consist of heading to
`https://python.org/` and downloading `version 2.7.11` and installing it. (not
`version 3`)

 

We then typed the word ‘`python`’ in to a command window (`cmd prompt`) to check
installation was successful, this returned to us the details of the version of
Python installed on our system.

 

Then for a small intro we proceeded to input the following directly in the `cmd
prompt` window:

 

>   The first part of this tells us which version of Python we have installed,
>   so make sure you have `version 2.7.x` installed. If not, install the right
>   version.

 

>   The second part, ‘`>>>`’ is showing us that we are now inside the Python
>   interpreter, and it will now accept Python statements. Try running a few
>   simple statements, remembering to press Enter after each one.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> message = "hello world"
>>> print message
hello world
>>>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

In the above example, we assigned the string *“hello world”* to the
variable *message* in the first line, and printed it in the second line.

 

>   We’re not limited to single line statements; we can also define functions
>   and run them.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> def print_message(message):
... print "I'm printing: " + message
...
>>> print_message('hello')
I'm printing: hello
>>>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

>   Remember that a function is defined by using def, the name of the function,
>   and then any arguments that the function takes. You can then call that
>   function.

 

>   Note the `<tab>` on the second line, and that you have to press `<Enter>`
>   after that line to exit the method. Also notice that we used double quotes
>   around “`I’m printing`”, because single quotes would have conflicted with
>   the apostrophe.

 

>   Doing anything other than very simple statements and programs is quite
>   fiddly using the command line, so it’s for this reason that we are going to
>   use `IDLE`.

 

Later on we will be using the built in `IDLE` editor that comes with Python.
