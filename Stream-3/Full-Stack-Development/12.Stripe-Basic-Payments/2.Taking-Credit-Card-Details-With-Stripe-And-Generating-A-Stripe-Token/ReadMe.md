### TAKING CREDIT CARD DETAILS WITH STRIPE AND GENERATING A STRIPE TOKEN

Normally, credit card details would need to be stored in a secure manner
somewhere on the server.

With Stripe, you send the details through using Stripes own secure channels and
the information never actually reaches your side of the setup.

The information is kept with Stripe and with the user’s web browser.
You’re simply passing a token or string that you can use in your transactions.

Let’s start by altering our registration form to allow us to take the details
that we’re going to pass to Stripe via their JavaScript API.  


![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452099024_image4.png)

  
We’re going to add four new fields, as you can see in the image above.

Add the following code to our UserRegistrationForm class in our
accounts/forms.py file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserRegistrationForm(UserCreationForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2015, 2036)]
 
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
 
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
 
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'stripe_id']
        exclude = ['username']
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   First, we’re generating some values for the months and years that will be
    used in our form for selecting the expiry details of our card. For each of
    these choices, we need to provide a list of pairs (tuples), where the first
    element is the value to store, and the second is the text to display to the
    user. In the case of months, we’ll use the month’s abbreviated name for the
    display value, and use the **enumerate** function to generate the numeric
    values. For the years, we’ll just use the same number for storage and
    display.

-   We also add a field for the credit card number and the CVV (the three digit
    number on the back of the card), and the actual fields for the expiry month
    and year.

-   We add a field for the stripe_id. As you can see, it uses the
    forms.HiddenInput widget to hide it from view as we will use it internally
    to store the token returned by Stripe later.

-   Finally, we add stripe_id to the list of form fields.

   
You can add additional fields to any ModelForm, but unless they’re part of the
Models fields, they will not be saved later!

 

### RETAINING OUR STRIPE ID

Because we want to save our stripe token/id for later use, we need to make a
small change to our derived User model in models.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
 
    objects = AccountUserManager()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we add in the stripe_id field as a CharField, so that when the registration
form is saved, we also retain our new token/id. Don’t forget to run your migrate
command once you update the User model.  


### VALIDATING CARD DETAILS

Next, we need to employ a little JavaScript to validate our credit card details
and obtain the stripe token/id.

First, we need to include a block in our *base.html* so that we only load the
JavaScript when we need it. To achieve this we need to do two things:

-   Copy the JQuery and BootStrap script links from the bottom of base.html and
    paste them into the \<head\>. Normally it’s a good policy to have our
    JavaScript links at the bottom of the file so we ensure that all our html
    elements have been rendered in the browser before any script executes that
    may target these elements. In this case we need to have the JQuery available
    for our own custom stripe validation script that we will create later in the
    topic.

-   Create a **head_js** block that we use to inject our JavaScript – including
    our JQuery immediately down into any child templates that need it upon being
    rendered. In our case, all the action takes place in register.html

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<head>
    <meta charset="utf-8">
    <title>Our Simple Site</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.6/cerulean/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    {% block head_js %}{% endblock %}
</head>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### CUSTOM FIELD VALIDATION SCRIPT

But before we get to edit our register.html file, we will create a custom
JavaScript file that uses JQuery to validate the stripe fields of our newly
modified registration form. This script is called when we click on the ‘Validate
Credit Card’ button on or registration form.

-   Create a new *static* directory at the root level.

-   Inside it, create a *js* subdirectory.

-   Inside *js* create a new file called *stripe.js*.

-   Register our *static* directory in settings, so it’s location is visible
    throughout the project.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static"),
)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Add the following code to stripe.js:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$(function() {
  $("#register-form").submit(function() {
      var form = this;   
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };
 
      $("#validate_card_btn").attr("disabled", true);
       Stripe.createToken(card, function(status, response) {
        if (status === 200) {
          console.log(status, response);
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          form.submit();
 
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
      });
      return false;    
  });
});
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we define that happens when the register-form is submitted.

-   Firstly, we want to collect the details into a JavaScript object called
    ‘card’, which we’ll add to the Stripe.createToken() function.

-   Before we do that though, we disable the validate card button so it isn’t
    triggered again while we wait for Stripe to assign us a token/id.

-   Then we do our actual call to Stripe using the createToken function, and
    after passing the card details, we create a handler function to control what
    happens when the request succeeds or fails.

-   After checking that the status was 200 (meaning it was a success), we then
    hide the errors part of the page in case it’s previously been shown, and
    then add the stripe token/id into the existing stripe_id field ready to be
    posted back to the server.

-   After that, we post the form back to the server to complete the registration
    process.

And in our *register.html*, we can now use the above to load in the Stripe
JavaScript API and our custom JavaScript that we create in our *static* files
folder.

The following changes are made:

-   We load the static files on line 3 to allow access our custom stripe.js
    script.

-   We add a template *head_js* block that includes stripe’s own payment
    processing javascript API on line 6.

-   Line 9 uses a variable called (unsurprisingly) Stripe which is used to
    capture and send back to the stripe server the STRIPE_PUBLISHABLE value that
    we declared in our *settings.py*earlier in the lesson. (Remember we got
    these values when we set up our new stripe account.) The {{ publishable }}
    variable will be set in our *register()* view over in *accounts/views.py*.

-   On line 12 we include our own stripe.js. This is used to target our form.

-   On line 16 we give our form an id = “register-form”. This id is used by our
    custom stripe.js file to target the form and its elements when validating
    and processing the payment details.

On line 17 we include a new div that will only be displayed if an error occurs
when trying to process a payment using stripe (e.g. as a result of invalid card
details).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{% extends "base.html" %}
{% load bootstrap_tags %}
{% load staticfiles %}
 
{% block head_js %}
  <script src="https://js.stripe.com/v2/" type="text/javascript"></script>
  <script type="text/javascript">
      //<![CDATA[
      Stripe.publishableKey = '{{ publishable }}';
      //]]>
  </script>
  <script type="text/javascript" src="{% static "js/stripe.js" %}"></script>
{% endblock %}
 
{% block content %}
  <form role="form" method="post" id="register-form" action="{% url 'register' %}">
    <div id="credit-card-errors" style="display:none">
      <div class="alert-message block-message error" id="stripe-error-message"></div>
    </div>
 
    <legend>Create a new account</legend>
    {% csrf_token %}
    {{ form|as_bootstrap }}
    <div class="form-group">
      <input class="btn btn-primary" id="validate_card_btn" name="commit" type="submit" value="Validate Credit Card">
    </div>
  </form>
{% endblock %}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This sets the scene up for our JavaScript to do some tidy work for us in getting
the token/id before we actually post the new registration details to the server
side to create our new user. Why do we care about the token/id? Well, as with
all API’s, the token is proof of identity when going through the API gateway.
