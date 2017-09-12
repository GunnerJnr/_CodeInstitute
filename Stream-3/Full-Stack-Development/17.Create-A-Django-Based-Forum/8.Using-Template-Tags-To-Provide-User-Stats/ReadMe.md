###  

### USE TEMPLATE TAGS TO PROVIDE USER STATS

By design, Django has restricted developers from using methods called from
object, etc. in templates. This effectively means that to perform any unusual
logic, you can’t just call a method from your model. Instead, you should use a
simple_tag or a filter for your template to do the needed processing.

In our example forum, we’re going to provide a human-readable way of telling
when posts and threads were created, the total amount of post submitted under a
subject, and also who was the last person to post on a thread. Btw, note that
we’re relying on each thread having at least one post; as a challenge, consider
whether that’s a good assumption, and whether it requires any special handling.

 

### A WALK THROUGH

Create a custom template tag python package in the threads folder
called *thread_extras*.

Now we add in three template tags:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import arrow
from django import template
 
register = template.Library()
 
@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
 
    return total_posts
 
@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()
 
@register.simple_tag
def last_posted_user_name(thread):
    last_post = thread.posts.all().order_by('created_at').last()
    return last_post.user.username
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

The first simply iterates through the threads contained in a subject and counts
up the number of posts contained in all the threads combined.

`started_time` uses arrow to return a simple ‘humanized’ version of the time,
since the supplied datetime objects time occurred – e.g., “Five minutes ago”, or
‘Just now’.

And finally, we filter all our posts from the supplied thread and order by
the `created_at` time to find the newest post in the thread, and return the
username of that user.

 

### SUMMARY

As you can see, there’s a lot you can achieve without even writing code and
‘standing on the shoulders of giants’, so to speak. With enough preparation, you
could prepare this basic forum into a package that you could install and
customise in subsequent projects. It’s because of this that Django is one of the
most popular web development frameworks in the world.
