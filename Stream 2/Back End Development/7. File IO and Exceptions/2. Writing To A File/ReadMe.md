WRITING TO A FILE
=================

 

We can also write to a file using the Python console.
Open **‘questions.txt’** in PyCharm and try writing to it using the console.

 

### Note:

To see changes to the text file as you use the Python console, you may need to
synchronize the file by pressing **ctrl + alt + y**.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> f = open('questions.txt')
>>> f.write('test')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: File not open for writing
>>> f = open('questions.txt','w')
>>> f.write('test')
>>> f.flush()
>>> f.tell()
4L
>>> f.write("\n")
>>> f.tell()
6L
>>> f.write('test 2')
>>> f.flush()
>>> f.writelines(['line1','line2','line3'])
>>> f.close()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Lines 2-5:** Trying to write to a file opened as read-only results in an
error.

**Line 8:** Sometimes, when you write to a file, the data isn’t saved to the
file immediately, but actually goes into a buffer. This buffer will be written
to the file when it reaches a certain size or when you close the file.

**Line 9:** There is also a pointer when writing to a file, and we can see that
it moves forward.

 

We’ll create a simple program that reads questions from the text file, and asks
the user. Put some questions and answers in the **questions.txt** file, for
instance:

 

Who invented the world wide web?

Tim Berners-Lee

 

Who invented the first mechanical computer?

Charles Babbage

 

Who invented the first computer mouse?

Douglas Engelbart

 

Make sure there are no blank lines in the file, as these will be counted as
lines. We’ll assume that the questions and answers are on alternate lines.

 

Here’s the code for parsing the questions:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_questions():
    questions, answers = [], []
    with open('questions.txt') as f:
        for i, line in enumerate(f):
            answers.append(line.strip()) if i % 2 else questions.append(line)
    return zip(questions, answers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 2: **Define two empty lists on the same line to hold our questions and
answers.

**Line 3:** Open the questions file using the with keyword as described
previously.

**Line 4:** If we just wanted to iterate through the lines in the file, we could
use for line in f, but we also want the line number, so that we can see whether
the line is a question (odd number) or answer (even number). The way to do this
is to use the enumerate keyword – now we are returning the line and the line
number.

**Line 5:** This line is a shorter way of writing:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if i % 2 != 0:
    answers.append(line.strip())
else:
    questions.append(line)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The **%** operator in Python means **‘remainder’**, so **i % 2** gives us the
remainder of dividing i by 2.

 

We can see this by using the Python console:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> 0%2
0
>>> 1%2
1
>>> 2%2
0
>>> 3%2
1
>>> 4%2
0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Obviously, there is no remainder when dividing an even number by two, so we can
tell which line is an answer and which is a question.

 

Notice that we strip the answer so that it doesn’t include **‘\\n’** – otherwise
all the answers will be wrong (because the user isn’t entering **‘\\n’** when
guessing)

 

**Line 6:** The
zip [function](http://codeinstitute.wpengine.com/glossary/function/) is a useful
way of merging two lists into one. Try using it in the console:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> zip(a,b)
[(1, 4), (2, 5), (3, 6)]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

It turns out there is an easier way of writing **get\_questions()**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_questions():
    with open('questions.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Instead of iterating over each line and deciding whether it’s a question or an
answer, we can iterate through a list 2 elements at a time.

Usually, range is used with just one argument, but we can use it with 2
arguments in the form **range(start, stop)**, or 3 arguments as **range(start,
stop, step)**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> range(6)
[0, 1, 2, 3, 4, 5]
>>> range(0,6)
[0, 1, 2, 3, 4, 5]
>>> range(3,6)
[3, 4, 5]
>>> range(0,3)
[0, 1, 2]
>>> range(0,6,2)
[0, 2, 4]
>>> range(1,6,2)
[1, 3, 5]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So we’re returning (line 1, line 2), then (line 3, line 4), then (line 5, line
6) all as a list.

 

Here’s a simple program that asks those questions, and counts the number of
questions correctly answered:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
questions = get_questions()
score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s out of %s questions right' % (score, total)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Try running the program and see if it works correctly.
