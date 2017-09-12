### ENABLE OR DISABLE SITE FUNCTIONALITY BASED ON A USER’S OWNERSHIP OF CONTENT AND LOGIN STATUS

Often you’ll want to restrict some of your site’s functionality based on the
visitor’s login status, or even restrict them from editing content that does or
does not belong to them. This is probably the most basic level of permissions
checking that most social sites allow.

So how do you actually do that with Django?

 

### OWNERSHIP PERMISSIONS

Checking for ownership is simply a case of checking whether the current object’s
user relationship is correct:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% if post.user == user or user.is_staff %}
… # show something
{% endif %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we also check if the user is a staff member, as we want posts to be
staff-moderated.

 

### LOGIN STATUS

In addition to using the \@login_required decorator on views that require an
authenticated user, we can also use the `is_authenticated()` method, which is
available anywhere you can access the user model.

When accessing in the templates, we need to omit the () section of the call, as
seen here:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
      {% if user.is_authenticated %}
        <p>
          <a href="{% url 'new_post' thread.id %}" class="btn btn-primary">New post</a>
        </p>
      {% endif %}
 
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
