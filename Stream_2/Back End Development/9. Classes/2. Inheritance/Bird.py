# create a class to handle our different bird types and the calls they make
class Bird:
    def __init__(self, bird_type, bird_call):
        self._bird_type = bird_type
        self._bird_call = bird_call

    def do_call(self):
        print 'a %s goes %s' % (self._bird_type, self._bird_call)

class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.learned_phrases = set()
        
    def learn_phrase(self, phrase):
        self.learned_phrases.add(phrase)
        
    def do_call(self):
        Bird.do_call(self)
        print '\n'.join(self.learned_phrases)
