### EXCEPTIONS

 

You’ve probably seen some exceptions already in your Python programs. The result
of an exception is that the program stops running and an error is shown in the
console.

 

Unfortunately, this isn’t very helpful to the end user of your software, who a)
won’t understand the error, and b) will be annoyed that the program has stopped
and possibly lost their work.

 

The solution to this is to catch exceptions when they happen and try to deal
with them. Try changing the name of the questions text file and see what
happens:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Traceback (most recent call last):
  File "C:/Users/will/PycharmProjects/quiz/quiz.py", line 19, in <module>
    questions = get_questions()
  File "C:/Users/will/PycharmProjects/quiz/quiz.py", line 14, in get_questions
    with open('wrong.txt') as f:
IOError: [Errno 2] No such file or directory: 'wrong.txt'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Ideally, we would like to avoid a message like this and help the user fix the
problem. We can do this by surrounding the code which is causing an exception in
a try-except block. PyCharm has a useful shortcut for surrounding text, **ctrl +
alt + t**:

 

![](img/1.png)

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_questions():
    try:
        with open('wrong.txt') as f:
            lines = f.readlines()
    except:
        print 'Questions file not found.'
        sys.exit()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]
 
 
questions = get_questions()
score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s out of %s questions right' % (score, total)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We try running the code in lines 3-4. If there is an exception, we catch it on
line 5 and run the code at lines 6-7. We use **sys.exit() **to exit the program
at line 7 because there aren’t any questions to ask.

 

Now, when you run the program with a non-existent questions file, you will get a
slightly more informative message.

 

There is still a slight problem with the program as it is though. There is
actually another way an exception could be caused – by having an odd number of
lines in the questions file.  If there are 7 lines in the questions file, then
i takes all the values in **range(0, 7, 2)**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> range(0, 7, 2)
[0, 2, 4, 6]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So now, when the following line is run, **lines[i+1]** will try to
access **lines[8]**, expecting an answer to be there, but it isn’t, and we will
get an index error.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Make sure the questions file is name correctly, then add another line to it and
see what happens. Our program is telling us that the question file isn’t found,
because it’s assuming that any error that occurs in **get\_questions** is
because of a missing file.

 

The problem is that our error handler is assuming that any error thrown
by **get\_questions** is because of a missing file. To solve this we can catch
specific errors in our handler:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
...
try:
    questions = get_questions()
except IOError:
    print 'Questions file not found.'
    sys.exit()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now, when you run the program, the error handler will let
the **IndexError** through, because it’s only able to catch the **IOError**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Traceback (most recent call last):
  File "C:/Users/will/PycharmProjects/quiz/quiz.py", line 23, in <module>
    questions = get_questions()
  File "C:/Users/will/PycharmProjects/quiz/quiz.py", line 19, in get_questions
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]
IndexError: list index out of range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can add another exception clause to catch the **IndexError**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:
    questions = get_questions()
except IOError:
    print 'Error: Questions file not found.'
    sys.exit()
except IndexError:
    print 'Error: All questions in the questions file must have answers.'
    sys.exit()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Python Exceptions are organised as a hierarchy:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can see that **IOError** is a subclass of **EnvironmentError**, which itself
is a subclass of **StandardError**, and **IndexError** is a subclass
of **LookupError**. We could use **LookupError** in our except clause instead
of **IOError**, but then it would be less specific.

 

If necessary, we can access the error type in our except clause, and perhaps
give the user a bit more information:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:
    questions = get_questions()
except IOError as e:
    print 'Error reading questions file: %s' % e
    sys.exit()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

### SUMMARY

In this lesson, you’ve learned:

-   How to open files in the correct mode and read or write to them.

-   How to use exceptions to handle error conditions, and use
    specific **except** clauses to catch different classes of errors.

 

### CHALLENGE

-   Write a program which allows the user to enter their own quiz questions,
    which are appended to the questions file. You will have to open the file
    using mode ‘w’ and use **f.write** or **f.writelines**.

-   Change the program so that the user has several guesses per question.

-   Detect if the answer is right but the spelling is wrong. For instance, if
    only 2 characters are different, allow this as a correct answer.

 

### HINT

There is a module called **difflib** which might help, or you can iterate
through both the guess and the answer at the same time comparing each letter
(note that they might have different lengths!).

 

### Please Note:

My actual solution will follow in the near future, due to work and time
restrictions I will be rushing through the course to get the content complete
and coming back to the solutions at a later date. Thanks
