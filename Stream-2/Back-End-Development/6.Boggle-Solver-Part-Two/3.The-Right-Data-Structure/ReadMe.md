The Right Data Structure
========================

 

So, what can we do? The bigger a List is, the longer it will take to search. In
fact, there’s a direct linear link between the size of a list and how long it
takes to search. But, we want big dictionaries. Big dictionaries mean more words
and better results.

 

**Lists** aren’t the only collections Python provides. A **Set** can provide
lookup that remains constant even when the size of the set increases. It does
this by managing
an [index](http://codeinstitute.wpengine.com/glossary/index/) of its contents
internally.

 

You don’t need to do very much different to benefit from this faster lookup; in
fact, you only need to change two characters.

 

Here’s the code that loads the dictionary:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_dictionary(dictionary_file):
    with open(dictionary_file) as f:
     return [w.strip().upper() for w in f]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Notice the **square brackets** on **line 3**. This is a Python list
comprehension. The resulting data structure will be a List.

 

Using a Set instead of a List is a simple matter of changing
the **[]** to **{}**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_dictionary(dictionary_file):
    with open(dictionary_file) as f:
     return {w.strip().upper() for w in f}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

That simple change will significantly improve the performance of our algorithm,
and the reason can be seen in the profiling results.
The **is\_a\_real\_word** [function](http://codeinstitute.wpengine.com/glossary/function/) is
no longer a significant portion of the running time of the algorithm. All of
that wasted time has been eliminated.

 

![](img/1.png)

 

### LISTS, SETS AND DICTS

 

Python **Lists** and **Dicts** can seem similar in terms of checking whether
they contain an element:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> l = ['item']
>>> 'item' in l
True
>>> d = {'item':True}
>>> 'item' in d
True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

But actually there is something very different going on under the hood.

 

To check whether an item is in a **list**, every item in the list is traversed
to see if it’s the right one. So for a large list with thousands of elements,
such as our dictionary, it’s going to take a lot longer to execute our line
‘**if word in dictionary**’. With a **dict**, it’s very quick to search for an
item and takes the same time, no matter how large the dict is.

 

A **set** is pretty much just a Python dict without the associated value. Like a
dict, you can’t have duplicate keys. Dicts and Sets work in the same way, and
are an example of a **Hash Table**. It’s beyond the scope of this course to
cover them, but you can read more about them
here: <https://en.wikipedia.org/wiki/Hash_table>

 

**Line 3**: We’re now using a Set comprehension rather than a List
comprehension. A set comprehension looks exactly like a dictionary
comprehension, but without the value – which is exactly what a Set is.

 

If you run it now, you should see a large speedup. On my machine, it went from 8
seconds to 0.5 seconds – just by changing two characters. Unfortunately, it’s
still too slow to run on a 4×4 grid, so we’ll have to carry on optimising.
