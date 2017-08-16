Django Blog, Part 1 – Intro
===========================

##### This is the first of a five-part lesson where the students begin to develop their own blog. In this section the students will begin setting up their Django models and admin panel, as well as writing some unit tests

 

### INTRODUCTION

Now let’s create something practical and useful with Django.

In this lesson, we are going to create a simple blog which will display both
summary and detailed views of each entry. Users will also be able to add blog
entries via a web form.

Each blog entry will consist of the following:

-   A creation date

-   A publish date (we may want to hold off publishing a blog entry until a time
    that suits)

-   The blog title

-   The blog content

All blog entries will be stored to and accessed from an SQLite database through
the use of models. We will use template inheritance when displaying our blog
entries. So let’s get started!

 

### CREATE A NEW PROJECT

1.  Create a new Django project called **blog_prj**

2.  Create an new app called **blog**

3.  Create a project superuser for admin access

Now that the framework basics are in place, let’s start fleshing out the blog
app components.

As per usual, register the blog app in **INSTALLED_APPS** within **settings.py**
