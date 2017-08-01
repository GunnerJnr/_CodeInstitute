Reading from a File
===================

 

Create a new Python file called **quiz.py**. We need a file to open so create a
text file called **‘questions.txt’** and add some lines to it.

 

For instance:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Line 1
Line 2
Line 3
Line 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now, add the following code to **quiz.py** and run it:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f = open('questions.txt', 'r')
lines = f.readlines()
f.close()
print lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

You should see the following output:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
C:\Python27\python.exe C:/Users/will/PycharmProjects/code_academy/quiz.py
['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n']
 
Process finished with exit code 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Let’s look at what’s happening on each line.

`f = open(‘questions.txt’, ‘r’)`

 

We use the **open** keyword to open a file. The first argument is the file name,
the second is the **mode**. File names can be **absolute** or **relative**. A
relative filename is relative to the current file – our program is expecting
questions.txt to be in the same folder as our program. But we could also use an
absolute file name:

`f = open(‘C:\Users\will\PycharmProjects\quiz\questions.txt’, ‘r’)`

 

There are pros and cons to each method. If I gave this program to someone else
and they ran it, it probably wouldn’t work because they will have a different
username, or they might have put the program and text file in a different folder
altogether.

 

The relative filename will work wherever the program has been put, as long as
the text file is in the same folder. However, if we decided to move our program
to a different folder but kept the text file in the same place, the absolute
path would still work, and the relative path wouldn’t.

 

Imagine if our program became very large and required several Python files in
different folders. We might move all the code that we use to open files into a
separate Python file called **‘open\_files.py’** and put it in a folder
called **‘utils’**. In this scenario the relative path used
in **‘open\_files.py’** will no longer work because the code is now in a
different folder to the file being opened, but our absolute path will still
work.

 

The second argument to **open** is the mode, which needs to be one of the
following:

| Mode    | Meaning        | Description                                                                                                         |
|---------|----------------|---------------------------------------------------------------------------------------------------------------------|
| r       | read           | Only allow reading from a file. If it doesn’t exist, there will be an error.                                        |
| w       | write          | Only allow writing to a file. If it doesn’t exist, a new one will be created                                        |
| a       | append         | Append to a file, e.g. write new content after the existing content. If it doesn’t exist, a new one will be created |
| r+      | read and write | Allow reading and writing to a file.  If it doesn’t exist, there will be an error.                                  |
| w+      | read and write | Same as r+ but a new file will be created if it doesn’t exist                                                       |
| rb / wb | binary         | Same as r/w but use binary instead of text (Windows only)                                                           |

 

It’s unlikely you’ll use anything other than r, w and a. Because ‘r’ is used
more often than the others, you can use open without the last argument to mean
read-only:

`f = open(‘questions.txt’)`

 

Notice that we get a variable back from the open command. This is called a file
handle and allows us to manipulate our file, as we see in the next line.

`lines = f.readlines()`

 

We call **readlines()** on our file handle which reads all lines into a list,
but there are many other methods:

-   **f.readline:** Read one line at a time

-   **f.read:** Read the entire file

-   **f.seek:** Seek to a particular point in the file

 

It’s important to understand that when you open a file, you are reading or
writing to a certain position within the file. If you use **readline** to read a
line, your position within the file as advanced by a line. The next time you
read a line, the line will be read from the end of the last line. It’s also
important to understand that files don’t really have lines. Files are just one
long line of characters, but when Python sees a line separator such as
‘**\\n**’, it splits the lines for us.

 

We can investigate this further by using the Python console:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f = open('questions.txt')
>>> f
<open file 'questions.txt', mode 'r' at 0x0242CBD0>
>>> f.tell()
0L
>>> f.readline()
'Line 1\n'
>>> f.tell()
8L
>>> f.readline()
'Line 2\n'
>>> f.readlines()
['Line 3\n', 'Line 4\n']
>>> f.seek(0)
>>> f.tell()
0L
>>> f.read(3)
'Lin'
>>> f.close()
>>> f
<closed file 'questions.txt', mode 'r' at 0x0242CBD0>
>>> f=open('questions.txt')
>>> f.mode
'r'
>>> f.read()
'Line 1\nLine 2\nLine 3\nLine 4\n'
>>> f.close()
>>> f.readline()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: I/O operation on closed file
>>> f=open('nonexistant.txt')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'nonexistant.txt'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 3:** We can see that **f** is an open file handle.

**Line 4:** **tell()** tells us our current file position, which we can see is
0.

**Lines 6-9:** After reading a line, our position is now 8, because the line was
8 characters long (‘Line 1’ + ‘\\n’).

**Lines 12-13:** Readlines returns a list of lines, from our last position.

**Lines 14-16:** We seek back to the start of the file, and this is confirmed by
using tell. Another way of seeking back the start is to close and reopen the
file again.

**Lines 17-18:** We can read a certain number of characters by
using **read(n)**.

**Lines 19-21:** We close the file, and the handle changes to reflect this.

**Line 23:** We can see what mode the file is opened in.

**Line 25:** Using read without an argument reads the entire file. We can see
here a more accurate representation of what the file actually looks like – a
long stream of characters.

**Line 28:** Trying to read from a close file results in an error.

**Line 32:** Trying to read from a non-existent file also results in an error.

 

Once you’ve opened a file in Python, it’s important to close it afterwards.
While you have a file opened, you can’t use it in any other program.

 

Try opening a file in the Python console but don’t close it. You should see the
following:

![](img/1.png)

 

An alternative to closing files manually is to use the **with** keyword,
otherwise known as a **context manager**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open('questions.txt') as f:
    lines = f.readlines()
print lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The idea is that instead of having to remember to close the file, the file is
closed automatically when leaving the block of code within
the **‘with’** clause. In this case, line 2 is the only block of code within the
with clause, so the file is automatically closed when moving to line 3 which is
outside the clause.

 

Another way of using the file handle is to iterate over it:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open('questions.txt') as f:
    for line in f:
        print line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
