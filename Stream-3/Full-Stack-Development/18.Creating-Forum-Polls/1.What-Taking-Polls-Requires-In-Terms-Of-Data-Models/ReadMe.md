###  

### WHAT TAKING POLLS REQUIRES IN TERMS OF DATA MODELS

When taking polls, we have a number of considerations that we need to bear in
mind.

Here’s a brief specification for what a poll should do:

-   Record users’ votes on a selection of subjects

-   Show the votes for each subject

So the basic requirements are pretty simple; but in reality, we need to store
data that allows us to accomplish this.

To store a poll, we should have at least three models:

1.  A **Poll model** to store the poll name

2.  A **Poll Subject model** to store what options are available to be voted on
    in our poll

3.  A **Vote model** to store the votes, so we can do a count up later when
    showing which subject is most popular, etc.

 

### RELATIONSHIPS

So now that we’ve defined our models, how will they relate to the current models
and to each other?

First off, our thread should be the main ‘parent’ of all these other models, as
each poll will be created inside a thread so people can cast their votes and
also discuss the subjects as the poll proceeds. With that in mind, we can create
a one-to-one relationship between the thread and the poll.

Next, the poll should be able to access the subjects as well as the votes.

This is so we can easily access the subjects when rendering our page. In
addition, we can easily count up the total votes for a poll if the poll is
linked to all votes with its subjects.

Querying for this then becomes as simple as:

poll.votes.count()

If we were to rely on the relationships in our subjects to do this, it would
still be possible to drill down, but wouldn’t be nearly as easy!

Finally, we want our subjects to be related to our votes in addition to the
poll, so that we can also make a simple call to Django’s ORM system, and get how
many votes each subject has received:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@register.filter
def vote_percentage(subject):
    count = subject.votes.count()
 
    if count == 0:
        return 0
 
    total_votes = subject.poll.votes.count()
 
    return (100 / total_votes) * count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So, all we need to do is use this nice and tidy template tag and we get a
percentage value when we display the poll’s subjects and their progress.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452784745_image1.png)

We’ll need to use it when supplying the percentage, but we’ll also need it for
when we set the width of the percentage bar beneath it.

Now that we have an idea of how to best set up models and relationships, we can
begin building our models and forms!  


### MODELS

So let’s start by creating a new app called polls and add it to our
INSTALLED_APPS. Then we’ll start defining our models based on our basic
specification:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.conf import settings
from threads.models import Thread
 
 
class Poll(models.Model):
 
    question = models.TextField()
    thread = models.OneToOneField(Thread, null=True)
 
    def __unicode__(self):
        return self.question
 
 
class PollSubject(models.Model):
 
    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='subjects')
 
    def __unicode__(self):
        return self.name
 
 
class Vote(models.Model):
 
    poll = models.ForeignKey(Poll, related_name="votes")
    subject = models.ForeignKey(PollSubject, related_name="votes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we have our Poll with a question, or perhaps a topic and a related field
for our thread.

We chose to call our subject `PollSubject` to avoid conflicting with the
threads’ Subject model too. That way, it’s always clear what the context of this
class is when we’re coding.

We’ve also established a link between the subject using a `ForeignKey` field,
because we will have one poll but many subjects.

Lastly, we have our `Vote` model, which relates back to our poll, subject, and
also the user that cast the vote so that we can do counting and also a bit of
checking later.

More on this subject later.

Don’t forget to run makemigrations and migrate!
