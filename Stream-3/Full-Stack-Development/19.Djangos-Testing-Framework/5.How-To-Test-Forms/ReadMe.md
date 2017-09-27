###  

How to Test Forms
=================

 

### HOW TO TEST FORMS

Next, we will need to create tests for any forms that we create – like our
registration form, for example.

The things we want to know are:

-   Does it validate properly with correct data is supplied?

-   Does it validate properly with incorrect supplied data?

-   Does the form clean properly?

In the case of our user registration form, we can see all of this at work:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserRegistrationForm(UserCreationForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2015, 2036)]
 
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
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise forms.ValidationError(message)
 
        return password2
 
    def clean_email(self):
        email = self.cleaned_data.get('email')
 
        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)
 
    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
 
        # automatically set to email address to create a unique identifier
        instance.username = instance.email
 
        if commit:
            instance.save()
 
        return instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

So first of all, let’s check the validation works for unfilled form fields with
a simple test to see if correct data works:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
 
 
class CustomUserTest(TestCase):
    ...
    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
 
        self.assertTrue(form.is_valid())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now add a missing value for our email:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
 
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can also do the same test for the two password fields.

 

And finally, a test for the passwords matching:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### SUMMARY

As you can see, testing can be tricky – especially when thinking about getting
started!

The main things you can do to think of tests to perform are to look at your
system and ask:

-   What should happen when this succeeds?

-   What should happen when this fails?

-   Are there any if or elses that need special conditions to be tested?

If you follow that route, you’ll soon have a pretty good set of tests that can
be run.
