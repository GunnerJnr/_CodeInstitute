=====
Blog
=====
 
Blog is a reusable blog app for Django
 
Detailed documentation is in the "docs" directory.
 
Quick start
-----------
 
1. Add 'reusable_blog' to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = (
        ...
        'reusable_blog',
    )
 
2. Include the polls URLconf in your project urls.py like this::
 
    url(r'^blog/', include('reusable_blog.urls')),
 
3. Run `python manage.py migrate` to create the blog models.
 
4. Add the blogs css::
    <link rel="stylesheet" href="{% static "css/blog.css" %}">
 
5. Add a link to the blog in the base.html
	<li><a href="/blog/">Our Blog</a></li>
 
6. Visit http://127.0.0.1:8000/blog/ to view the blogs you create.