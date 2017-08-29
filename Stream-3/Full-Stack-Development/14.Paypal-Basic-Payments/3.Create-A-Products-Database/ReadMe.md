Create a Products Database
==========================

##### In this unit the students will learn how to build up a database of products that can be sold using Paypal

 

### CREATE A PRODUCTS DATABASE

In addition, we’re going to create a list of products that we can display on the
front page of our site.  Each will have its own *Buy Now* PayPal button that
will start off the payment process.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452113330_image5.png)

Firstly we’ll create a new app called *products* and add it to INSTALLED_APPS in
the settings.py file. Then we’ll create our Product model in the models.py file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
 
 
class Product(models.Model): 
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the basis of most products you’ll ever manage in a system, but you may
find yourself adding other things like images, etc. in projects of your own.
We’ll keep it simple for now, though.

Now let’s create a new directory in the templates directory and call
it *products*. Next we’ll create a new HTML file and call it *products.html*.

On our *products* list page, we’ll simply list each item and put a Buy Now
button next to it so that the user can purchase the item.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% block content %}
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Price</th>
                <th>Purchase</th>
            </tr>
        </thead>
        <tbody>
            {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>{{ product.description }}</td>
                    <td>${{ product.price }}</td>
                    <td>{{ product.paypal_form.sandbox }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we use the bootstrap class `table` and `table-striped` to apply some
formatting to our table. Everything else should be pretty familiar by now –
except for the line that read:

`<td>{{ product.paypal_form.sandbox }}</td>`

This is something different! It’s a property we’ve created on the model that
supplies a Django form to render our button.

   
The end of that statement ends in `.sandbox`. This means that our button is set
to send all transactions to the test side of PayPal. In a production
environment, this should use the `.render` method to point all customers to the
real PayPal handling systems, as in:

`<td>{{ product.paypal_form.render }}</td>`

So how did we define that property? In our Product model we add:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
 
...
 
    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }
 
        return PayPalPaymentsForm(initial=paypal_dict)
 
    def __unicode__(self):
        return self.name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the `@property` decorator to define a function that can be accessed from
our template, we prepare a dict that contains the following:

-   **business**: the email address of our merchant

-   **amount**: the price of our production

-   **currency**: USD in our case!

-   **item_name**: the item’s … name!

-   **Invoice**: A string to uniquely identify our transaction. In our case,
    we’re combining the primary key value of our product and a randomly
    generated unique id

-   **notify_url**: where PayPal can send any success or error messages on our
    site

-   **return_url**: where to return a customer after the payment process is
    complete

-   **cancel_url**: where to return the customer if they choose to cancel the
    payment process

We use this to pass the needed information for the PayPalPaymentsForm to create
our button, and also the required html form markup when we render the page
template.

Now we’ll create the url for our products by creating a new url in our
we_are_social urls.py file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from products import views as product_views
 
urlpatterns = [
    ...
    url(r'^products/$', product_views.all_products)
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we’ll just create a view called `all_products` in our products views.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from .models import Product
 
 
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lastly, what we need to do is update our base.html file so we’ll have a link
that will bring us to our products page. Inside our nav bar we’ll create a new
link:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<ul class="nav nav-pills pull-right">
    ...
    <li><a href="/products/">Products</a></li>
    ...
</ul>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### POPULATING PRODUCTS

In order to enable the Products model in the admin, we also need to add some
code to our admin.py in the products app folder:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from models import Product
 
admin.site.register(Product)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
