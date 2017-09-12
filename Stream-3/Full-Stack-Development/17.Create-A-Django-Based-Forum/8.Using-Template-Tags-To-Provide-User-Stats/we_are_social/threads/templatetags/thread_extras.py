import arrow
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
def get_total_subject_posts(subject):
    """
    get_total_subject_posts():
    """
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts


@register.filter
def started_time(created_at):
    """
    started_time():
    """
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    """
    last_posted_user_name():
    """
    last_post = thread.posts.all().order_by('created_at').last()
    return last_post.user.username
