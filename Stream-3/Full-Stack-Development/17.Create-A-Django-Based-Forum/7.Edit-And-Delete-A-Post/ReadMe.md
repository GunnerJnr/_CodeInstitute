###  

Edit and Delete a Post
======================

##### In this unt the students ill learn how to edit and delete posts in their Django blog

 

### EDIT AND DELETE A POST

We now return to the *comment_details.html* template referenced in
our *post.html*.

Create a *comment_details* template in your *forum* directory and add the code
below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% load thread_extras %}
<div class="details">
   <div class="col-md-6">
       <div class="pull-left">
           <time datetime="{{ post.created_at }}">
              Posted: {{ post.created_at|started_time }}
           </time>
       </div>
   </div>
   <div class="col-md-6">
       <div class="pull-right">
         {% if post.user == user or user.is_staff %}
           <a href="{% url 'edit_post' thread.id post.id %}"><i class="fa fa-pencil-square-o"></i></a>
           <a href="{% url 'delete_post' thread.id post.id %}"><i class="fa fa-trash-o"></i></a>
         {% endif %}
       </div>
   </div>
   <div class="clearfix"></div>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the code above, we refer to 2 font-awesome icons (CSS classes):

1.  fa-pencil-square-o

2.  fa-trash-o

These icons represent edit and delete actions. If the user logged in is the
owner of the post or an admin, they can edit or delete the post.

While we need to create a view/url pattern combination for
both `edit_post` and `delete_post`, neither view requires a unique template.

Create the *edit_post* view in *threads/views.py*:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@login_required
def edit_post(request, thread_id, post_id):
   thread = get_object_or_404(Thread, pk=thread_id)
   post = get_object_or_404(Post, pk=post_id)
 
   if request.method == "POST":
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           messages.success(request, "You have updated your thread!")
 
           return redirect(reverse('thread', args={thread.pk}))
   else:
       form = PostForm(instance=post)
 
 
   args = {
       'form' : form,
       'form_action': reverse('edit_post',  kwargs={"thread_id" : thread.id, "post_id": post.id}),
       'button_text': 'Update Post'
   }
   args.update(csrf(request))
 
   return render(request, 'forum/post_form.html', args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *edit_post* view refers back to *post_form.html*.

The *edit_post* url pattern:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *delete_post* view:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@login_required
def delete_post(request, thread_id, post_id):
   post = get_object_or_404(Post, pk=post_id)
   thread_id = post.thread.id
   post.delete()
 
   messages.success(request, "Your post was deleted!")
 
   return redirect(reverse('thread', args={thread_id}))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

renders the thread view/template.

The *delete_post* url:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
