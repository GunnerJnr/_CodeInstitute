# create a class to handle our different bird types and the calls they make
class Bird:
    def __init__(self, bird_type, bird_call):
        self._bird_type = bird_type
        self._bird_call = bird_call

    def do_call(self):
        print 'a %s goes %s' % (self._bird_type, self._bird_call)
