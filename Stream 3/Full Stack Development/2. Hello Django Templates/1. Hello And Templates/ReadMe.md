Hello %s! and Templates
=======================

##### In this unit the students will learn the basics of Django templates

### HELLO %S! AND TEMPLATES

Just before we look at templates, let’s look at how we can add variable content
to a view.

Update the view you created in the last lesson with the code shown below:

![pycharm-%s.png](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455123360_image1.png)

The function has been modified to use two variables, and the code within the
view constructs an HTML response using Python’s “format-string” capability.
The **%s** within the string is a placeholder, and the percent sign after the
string means “Replace the %s placeholder in the string with the value held in
the name variable.”

Start your server and test your changes. You should see something similar to
below:

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455123360_image2.png)

We can see that the text was rendered dynamically through the use of a variable
and some HTML content hard-coded into our view.

   
In our next lesson, which covers Django Models, we’ll learn how to display data
from a database. But for now, our data will be defined within our views.

### TEMPLATES

The last example is a good illustration of how you can add dynamic content to a
view. But we really shouldn’t be hard-coding HTML in our views and here’s why:

Sites are living entities and evolve over time. A site’s interfaces will
probably change a lot more than its underlying Python code. By using the above
approach, any design changes to the page require a change in the Python code.
The design is what we call tightly coupled to the code. It would be much better
if we could decouple the design elements from the underlying code.

Larger projects often involve a delegation of responsibilities amongst the
development team, where each member may have a particular strength. Python
coding proficiency and HTML design chops are two different disciplines, and not
everyone will have a full stack skillset. For the others, we should not expect a
designer to edit Python when making changes.

By separating the concerns through the use of templates, we get stuff done
faster if we don’t, say, have a designer waiting on a Python developer to
provide underlying functionality.

A Django template is just a text file and can generate any text-based format
(HTML, XML, CSV, etc.).

Templates are used to separate the presentation of a document from its data and
logic. A  template defines placeholders and logic through the use of template
tags and variables that determine how the document is rendered.

### TEMPLATE PHILOSOPHY

The following is taken from the [Django
Book](http://www.djangobook.com/en/2.0/index.html):

The template system has roots in how web development is done at World Online and
the combined experience of Django’s creators. Here are a few of those
philosophies:

-   Business logic should be separated from presentation logic. Django’s
    developers see a template system as a tool that controls presentation and
    presentation-related logic, and that’s it. The template system shouldn’t
    support functionality that goes beyond this basic goal.

-   For that reason, it’s impossible to call Python code directly within Django
    templates. All “programming” is fundamentally limited to the scope of what
    template tags can do. It is possible to write custom template tags that do
    arbitrary things, but the out-of-the-box Django template tags intentionally
    do not allow for arbitrary Python code execution.

-   Syntax should be decoupled from HTML/XML. Although Django’s template system
    is used primarily to produce HTML, it’s intended to be just as usable for
    non-HTML formats, such as plain text. Some other template languages are XML
    based, placing all template logic within XML tags or attributes, but Django
    deliberately avoids this limitation. Requiring valid XML to write templates
    introduces a world of human mistakes and hard-to-understand error messages,
    and using an XML engine to parse templates incurs an unacceptable level of
    overhead in template processing.

-   Designers are assumed to be comfortable with HTML code. The template system
    isn’t designed so that templates necessarily are displayed nicely in WYSIWYG
    editors such as Dreamweaver. That is too severe a limitation and wouldn’t
    allow the syntax to be as friendly as it is. Django expects template authors
    to be comfortable editing HTML directly.

-   Designers are assumed not to be Python programmers. The template system
    authors recognize that Web page templates are most often written by
    designers, not programmers, and therefore should not assume Python
    knowledge.

-   However, the system also intends to accommodate small teams in which the
    templates are created by Python programmers.

-   The goal is not to invent a programming language. The goal is to offer just
    enough programming-esque functionality, such as branching and looping, that
    is essential for making presentation-related decisions.
