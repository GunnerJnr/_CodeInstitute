No Challenge 
=============

 

Although this lesson had no challenge, it did have a walk through. The walk
through consisted of explaining a bit about the command line, what an
‘`Environment Variable`’ is (e.g. `%PATH%`). Below are the listed steps we
followed so you can have an idea on what was achieved in the command line.

 

### PATH

You may have noticed that Python was installed to `C:\Python27\`, and yet Python
still runs from this directory.

  
This is because `python.exe` was added to the `PATH environment variable`. An
`environment variable` is just a value, like a string in Python.
The `PATH` `environment variable` contains a list of folders which should be
searched when we run a command.

 

For Windows, it looks like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c:\Windows\System32\>; echo %PATH%
c:\WINDOWS\system32;C:\WINDOWS;c:\Python27;C:\Python27\Scripts;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

For Mac and Linux, it looks like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ echo $PATH
/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

>   *If you’re using Mac OS or Linux, your directories are separated by forward
>   slashes “*`/`*”. Windows operating systems use the backslash “*`\`*” to do
>   the same thing.*

 

The `echo` command is similar to `print`* *in Python. We are just printing the
variable called `PATH`.

 

In Windows, we have to enclose it in `%` to distinguish it from a plain string.

 

Try omitting them and see what happens:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c:\Windows\System32>echo PATH
PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Similarly for Mac and Linux, we use the “`$`” sign:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ echo PATH
PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Your `PATH` will probably look different to the ones shown here, but you should
see the Python entries.

 

### CHANGE DIRECTORY

Let’s jump to `C:\Python27` and see what’s inside. To do this we use the change
directory command `cd` to take us our our location.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c:\Windows\System32>;cd c:\Python27\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

>   *Typing *`cd ..`* will navigate up one level in your directory tree.
>   Typing *`cd ..\..`* (Win) *`cd ../..`*(Mac/Linux) will bring you up two
>   levels, and so on…*

 

### VERIFY DIRECTORY CONTENTS

To view the contents of a directory in Windows, we use the `dir` command. For
Mac and Linux, we use `ls`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c:\Windows\System32>cd c:\Python27\                      
 
c:\Python27>;dir                                          
 Volume in drive C is Windows                            
 Volume Serial Number is CC9E-415C                       
 
 Directory of c:\Python27                                
 
02/09/2015  12:16    <Dir>          .                    
02/09/2015  12:16    <Dir>          ..                   
02/09/2015  12:16    <Dir>          DLLs                 
02/09/2015  12:16    <Dir>          Doc                  
02/09/2015  12:16    <Dir>          include              
02/09/2015  12:16    <Dir>          Lib                  
02/09/2015  12:16    <Dir>          libs                 
23/05/2015  10:24            38,584 LICENSE.txt          
23/05/2015  10:23           418,960 NEWS.txt             
23/05/2015  09:40            26,624 python.exe           
23/05/2015  09:40            27,136 pythonw.exe          
10/05/2015  18:01            53,986 README.txt           
02/09/2015  12:16    <Dir>          Scripts              
02/09/2015  12:16    <Dir>          tcl                  
02/09/2015  12:16    <Dir>          Tools                
23/05/2015  09:39            49,664 w9xpopen.exe         
               6 File(s)        614,954 bytes            
              10 Dir(s)   7,076,974,592 bytes free       
 
c:\Python27>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

>   *Pressing the up and down arrow keys will scroll through your command
>   history, so you don’t have to type in the same command twice. Pressing tab
>   while typing a *`filename`* will try to complete the *`filename`* for you.*

 

>   *If you’re on Windows and find you’re using the command line a lot, you
>   might want to install an alternative command line such as ConEmu
>   (*`https://conemu.github.io/`*), which provides more features such as tabs,
>   copy and paste, and colors.*
