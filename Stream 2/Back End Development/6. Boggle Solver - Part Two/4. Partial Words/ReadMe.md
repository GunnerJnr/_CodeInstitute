Partial Words
=============

 

Loading the dictionary into a **Set** instead of a **List** has improved the
performance of our algorithm. We can search a 4×4 grid, but it’s still too slow.
We need to dig a bit deeper.

 

During the search, we build up paths through the grid, by adding letters one at
a time and seeing if the new path represents a word in the dictionary. If we
knew at any point that no words in the dictionary start with the current path
we’re constructing, we would know that searching any further down that path is
futile, and we could abandon that path.

 

This would dramatically prune the search space.

 

We can implement this idea in a kind of naive way to see if it has any effect.
Before we do, let’s run the profiler for a 4×4 grid and make a note of the
running time. This will be our baseline to compare optimisations against.

 

![](img/1.png)

 

About 53 seconds for a 4×4 grid. Too slow. But, we know where we stand.

 

Here’s a simple implementation of our ‘**Start of word**’ idea. *Don’t code
this *[function](http://codeinstitute.wpengine.com/glossary/function/)* just
yet:*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_start_of_a_real_word(word, dictionary):
    for item in dictionary:
        if item.startswith(word):
            return True
    return False
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We iterate through the dictionary, and check if any entry starts with the
letters we’re checking. If we get through all the items in the dictionary and
don’t find a match, then there is no point adding more letters to this path
because no word starts with the letters we have.

 

If you’re paying attention you might be thinking, “Hey! We changed from a List
to a Dictionary to avoid this kind of sequential searching, and here we are
doing it again!”

 

And you’d be right. This isn’t a good approach. Let’s not do it this way. We can
be a little more clever and get all the benefits without this linear searching
creeping back into the code.

 

### PRECALCULATING WORD STEMS

 

We know we can check for words starting with the current path by linearly
searching the dictionary. The last time we needed to a linear search, we used a
dictionary to solve the problem. We’re going to do the same again. We’re going
to create a second dictionary that contains all of the partial words (we’ll call
them stems).

 

If the dictionary contains the words:

**BUS**  
**THIS**

The stems dictionary would contain:

**B**  
**BU**  
**T**  
**TH**  
**THI**

 

If this ‘**Stems**’ dictionary existed, we could do a constant time lookup of
any partial word, rather than the linear time lookup we implemented above.

 

### NOTE:

We’re about to do some significant modifications to our code. Run all your Unit
Tests at this point to make sure everything passes before we start.

 

Here you can see the
modified **get\_dictionary** [function](http://codeinstitute.wpengine.com/glossary/function/),
which now returns **stems** in addition to **full\_words**:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_dictionary(dictionary_file):
    full_words, stems = set(), set()
 
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
 
            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words, stems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The **get\_dictionary** [function](http://codeinstitute.wpengine.com/glossary/function/) is
now returning a tuple of two Sets, one containing full words and another
containing stems (partial words). We’ll have to modify our call
to **get\_dictionary** to allow for this different return type. Here’s the full
code of the new
search [function](http://codeinstitute.wpengine.com/glossary/function/):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
 
    def do_search(path):
        word = path_to_word(grid, path)
        if is_a_real_word(word, full_words):
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
 
    for position in grid:
        do_search([position])
 
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

On **Line 4**, we unpack the dictionary tuple into the stems and full words.

 

One **Line 8**, we use **full\_words** to check if we’ve found a real word.

 

On **Line 10**, we use stems to see if we can ignore the rest of the path we’re
on.

 

### A FAILING TEST

 

If you run your Unit Tests now, you’ll find one test fails.

 

![](img/2.png)

 

The **test\_search\_grid\_for\_words** test creates a mock dictionary that no
longer matches the tuple of two sets that the program now uses.

 

A simple fix (though not the best one) is to modify the test to include the
stems of the test words:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_search_grid_for_words(self):
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = "EEE"
 
        fullWords = [twoLetterWord, threeLetterWord, notThereWord]
        stems = ['A', 'AB', 'E', 'EE']        
        dictionary = fullWords, stems
 
        foundWords = boggle.search(grid, dictionary)
 
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will make the test pass, but it suffers from the same problem as the
original test. The internal implementation of our dictionary has leaked out into
our test – so when we change that implementation, the test has to change too.

 

One of the challenges below is to consider how we can modify our code to prevent
this
leaky [abstraction](http://codeinstitute.wpengine.com/glossary/abstraction/),
and isolate our tests from implementation details.

 

**COMPLETED CODE (from code institute)**  
The code for this lesson can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit06-Boggle_pt_2>

 

Please Note:

 

This is the solution of the code institute, my actual solution will follow in
the near future, due to work and time restrictions I will be rushing through the
course to get the content complete and coming back to the solutions at a later
date. Thanks
