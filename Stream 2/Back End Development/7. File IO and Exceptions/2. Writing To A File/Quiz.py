# open the file for reading using: open('file to open', 'mode')
# r | read | Only allow reading from a file
# w | write | Only allow writing to a file
# a | append | Append to a file
# r+ | read + write | Allow reading and writing to a file
# w+ | read + write | Same as r+ but will create new file if one doesn't exist
# rb / wb | binary | same as r/w but binary instead of text (windows only)
# dont specify mode for read only
# f = open('Questions.txt', 'r')

# read all lines of the file
# can also use:
# f.readline() - one line at a time
# f.read() - read entire file
# f.seek - seek a particular point in the file
# lines = f.readlines()

# close the file when we are finished reading/writing
# f.close()

# print the contents of the file to the console
# print lines

# define a method which gets the text file and reads the contents
def get_questions():
    with open('questions.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]

# we set the questions to our method to print out each question
# then we check to see if the entered answer is correct by checking
# it against the answer in the text file
questions = get_questions()
score = 0
total = len(questions)
for question, answer in questions:
    guess = raw_input(question)
    if guess == answer:
        score += 1
print 'You got %s out of %s questions right' % (score, total)
