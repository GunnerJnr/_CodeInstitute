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
