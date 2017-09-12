# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from threads.models import Subject, Thread, Post
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import ThreadForm, PostForm


# Create your views here.
def forum(request):
    """
    forum(): pull the all subjects from the database and pass them to our view
    """
    return render(request, 'forum/forum.html', {'subjects': Subject.objects.all()})


def threads(request, subject_id):
    """
    threads():
    """
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/threads.html', {'subject': subject})


@login_required
def new_thread(request, subject_id):
    """
    new_thread():
    """
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            messages.success(request, "Your have create a new thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        thread_form = ThreadForm()
        post_form = PostForm()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
    }
    args.update(csrf(request))

    return render(request, 'forum/thread_form.html', args)
