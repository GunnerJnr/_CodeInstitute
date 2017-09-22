###  

What the Process of Taking a Poll Requires to be Accurate
=========================================================

### WHAT THE PROCESS OF TAKING A POLL REQUIRES TO BE ACCURATE

Finally, let’s take a look at something that might not be obvious about taking
polls… accuracy!

When we take a poll, we supply a link to the voting button that allows us to
pass our vote on the subject. That works great until we start visiting the page
again and again and clicking the button some more. Suddenly, our poll’s voting
calculations aren’t really that true anymore!

To stop this, we ensure that we take a record of whom it was that sent the vote.
Create a new view called `thread_vote` in *threads.views.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from polls.models import PollSubject
...
@login_required
def thread_vote(request, thread_id, subject_id):
   thread = Thread.objects.get(id=thread_id)
 
   subject = thread.poll.votes.filter(user=request.user)
 
   if subject:
       messages.error(request, "You already voted on this! ... You’re not trying to cheat are you?")
       return redirect(reverse('thread', args={thread_id}))
 
   subject = PollSubject.objects.get(id=subject_id)
 
   subject.votes.create(poll=subject.poll, user=request.user)
 
   messages.success(request, "We've registered your vote!")
 
   return redirect(reverse('thread', args={thread_id}))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

If it’s a poll the user has already voted on, then send them the error message
back.

When we render, we hide the voting buttons from our view. Add a new custom
template tag called `user_vote_button` to *thread_extras* as per below:  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@register.simple_tag
def user_vote_button(thread, subject, user):
   vote = thread.poll.votes.filter(user_id=user.id).first()
 
   if not vote:
       if user.is_authenticated():
           link = """
           <div class="col-md-3 btn-vote"> 
           <a href="%s" class="btn btn-default btn-sm">
             Add my vote!
           </a>
           </div>""" % reverse('cast_vote', kwargs={'thread_id' : thread.id, 'subject_id':subject.id})
 
           return link
 
   return ""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

But – you might be wondering why we still check in our view? After all, if we
only show the buttons, then there’s no vote recorded!

The answer is that we may or may not have a clever user who has figured out that
sending multiple requests to our *thread_vote* url would enable them to fix the
poll scores.

By checking again, we ensure that they can’t vote on the same poll more than
once, even if they tried.

To actually display the poll to the user, we modify the *thread.html* template.
Add the code from lines 46 -70 to your template:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load staticfiles %}
{% load thread_extras %}
{% block content %}
 
   <div class="row header"
       <div class="container">
           <h2>{{ thread.name }}</h2>
           <div class="col-md-12">
               <table class="table">
                   <tbody>
                   <tr>
                       <th>
                           CREATED
                       </th>
                       <th>OWNER</th>
                       <th>LAST POST</th>
                   </tr>
                   <tr>
                       <td>
                           <time datetime="{{ thread.created_at }}">
                           </time>
                       </td>
                       <td>{{ thread.user.username }}</td>
                       <td>{% last_posted_user_name thread %}</td>
                   </tr>
                   </tbody>
               </table>
           </div>
           {% if thread.poll %}
               <div class="container">
                   <div class="col-md-6">
                       <h2>Poll</h2>
                       <strong>{{ thread.poll.question }}</strong><br><br>
 
                       <p>Here’s how the votes are so far:</p>
                     {% for subject in thread.poll.subjects.all %}
                           <div class="col-md-10">
                               <strong>{{ subject.name }}</strong>
                               <span class="pull-right">{{ subject|vote_percentage }}%</span>
                           </div>
 
                           {% autoescape off %}
                           {% user_vote_button thread subject user %}
                           {% endautoescape %}
 
                        <div class="col-md-10">
                         <div class="progress">
                           <div class="progress-bar progress-bar-info" role="progressbar"
                            aria-value="{{ subject|vote_percentage }}" aria-valuemin="0"
                            aria-valuemax="100" style="width:{{ subject|vote_percentage }}%;">
                           </div>
                         </div>
                        </div>
                      {% endfor %}
                   </div>
               </div>
           {% endif %}
 
           {% if user.is_authenticated %}
               <p>
                   <a href="{% url 'new_post' thread.id %}" class="btn btn-primary">New post</a>
               </p>
           {% endif %}
       </div>
   </div>
   <div class="container">
       {% for post in thread.posts.all %}
           {% include "post.html" %}
       {% endfor %}
   </div>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Then we would like to see how users are voting on the poll.

First, we add a new filter to *thread_extras* as per below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@register.filter
def vote_percentage(subject):
   count = subject.votes.count()
   if count == 0:
       return 0
   total_votes = subject.poll.votes.count()
   return (100 / total_votes) * count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Finally, add the url pattern used to cast your vote:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Run your code to test. Don’t forget to set breakpoints across your files to
track down, isolate, and fix any bugs that might occur.

 

### SUMMARY

In this unit, we’ve seen how a bit of planning and forethought can assist you in
making a potentially complex task a great deal simpler. You can use your data
models to great effect and make the coding so simple that it’s easy to get the
answers you need without sacrificing the readability.

This is really what Python is all about – speed, simplicity, and readability.
