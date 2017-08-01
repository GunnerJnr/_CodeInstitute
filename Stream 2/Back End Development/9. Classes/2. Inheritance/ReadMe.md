Inheritance
===========

 

Subclassing is a useful way of creating a specialised version of a class with
it’s own methods but re-using existing methods of the parent class:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Here we’ve created a **Parrot **class which subclasses **Bird**. We can use the
existing methods on the parent class, and we don’t have to supply the bird name
and class because that’s coded into the **Parrot** class:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> class Parrot(Bird):
        def __init__(self):
            Bird.__init__(self, 'Parrot', 'Kah!')
>>> parrot = Parrot()
>>> parrot.do_call()
a Parrot goes Kah!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can also add specialised behaviour, and override existing methods:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> class Parrot(Bird):
        def __init__(self):
            Bird.__init__(self, 'Parrot', 'Kah!')
            self.learned_phrases = set()
        def learn_phrase(self, phrase):
            self.learned_phrases.add(phrase)
        def do_call(self):
            Bird.do_call(self)
            print '\n'.join(self.learned_phrases)
 
>>> parrot = Parrot()
>>> parrot.do_call()
a Parrot goes Kah!
 
>>> parrot.learn_phrase("I'm a pretty polly")
>>> parrot.learn_phrase("Who's a pretty boy, then?")
>>> parrot.do_call()
a Parrot goes Kah!
Who's a pretty boy, then?
I'm a pretty polly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 4**: Parrots can learn phrases, so we initialise an empty set in the
initializer.

 

**Lines 5-6:** This is a method specific to the **Parrot** class which allows it
to learn a phrase, and adds it to the set.

 

**Lines 7-9:** We override the **do\_call** method of the parent class so that
the learned phrases are printed after the call.
