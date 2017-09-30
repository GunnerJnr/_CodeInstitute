# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


# Create your views here.
def post_list(request):
    """
    Create a view that will return a list of
    Posts that were published prior to 'now' and
    render them to the 'blogposts.html' template
    :param request:
    :return:
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blog/blogposts.html", {'posts': posts})


def post_detail(request, slug):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, slug=slug)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})


def display_top_five_posts(request):
    """
    we wnat to get and list the top five most popular
    blog posts and display them in blogpost.html on clicking the
    link in the navigation menu
    :param request:
    :return:
    """
    top_posts = Post.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-views')[:5]
    return render(request, "blog/blogposts.html", {'posts': top_posts})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect(post_detail, post.pk)
            return redirect('post-detail', post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html', {'form': form})


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post-detail', post.slug)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blogpostform.html', {'form': form})
