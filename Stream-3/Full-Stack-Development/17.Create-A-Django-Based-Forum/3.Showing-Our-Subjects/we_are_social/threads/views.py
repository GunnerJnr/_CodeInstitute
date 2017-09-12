# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from threads.models import Subject, Thread, Post
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf


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
    pass
