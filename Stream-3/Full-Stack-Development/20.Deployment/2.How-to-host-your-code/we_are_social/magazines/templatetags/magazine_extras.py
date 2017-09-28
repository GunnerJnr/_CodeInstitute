import uuid

from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

register = template.Library() # pylint: disable-msg=C0103


def paypal_form_for(magazine, user):
    if user.is_subscribed(magazine):
        html = "Subscribed!"
    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "USD",
            "cmd": "_xclick-subscriptions",
            "a3": magazine.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "item_name": magazine.name,
            "invoice": uuid.uuid4,
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel-return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (magazine.pk, user.id),
        }

        if settings.DEBUG:
            # if we're in debug mode, we use the sandbox() method to return html for the form
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').sandbox()
        else:
            # If we're not debugging (as in live on a production server), we use render() to
            # give us a form that points to the live PayPal systems
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').render()

    return html

register.simple_tag(paypal_form_for)
