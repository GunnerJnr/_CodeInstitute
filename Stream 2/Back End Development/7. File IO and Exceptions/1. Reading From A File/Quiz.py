# open the file for reading using: open('file to open', 'mode')
# r | read | Only allow reading from a file
# w | write | Only allow writing to a file
# a | append | Append to a file
# r+ | read + write | Allow reading and writing to a file
# w+ | read + write | Same as r+ but will create new file if one doesn't exist
# rb / wb | binary | same as r/w but binary instead of text (windows only)
# dont specify mode for read only
f = open('Questions.txt', 'r')

# read all lines of the file
# can also use:
# f.readline() - one line at a time
# f.read() - read entire file
# f.seek - seek a particular point in the file
lines = f.readlines()

# close the file when we are finished reading/writing
f.close()

# print the contents of the file to the console
print lines
