### TAKING A SINGLE PAYMENT WHEN A NEW USER REGISTERS WITH PAYPAL

Now when we login to the admin, we’ll be able to add in a few dummy products to
test our buttons.

At this point, we’ve done most of the leg work in connection to taking the
actual payment. If the customer was to click the Buy Now button, they could
successfully buy our product. However, our website wouldn’t know about it, so we
need to record what happens when the user completes the payment.

For a simple one-off payment, we can use the return_url page for this as PayPal
posts all the transaction confirmation info back to that page when the user
returns to our site.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<QueryDict: {u'protection_eligibility': [u'Ineligible'], u'last_name': [u'Hibbert'], u'txn_id': [u'7PC450130C6830542'],u'receiver_email': [u'merchant@somesite.com'], u'payment_status': [u'Completed'], u'payment_gross': [u'2.30'], u'tax': [u'0.00'],u'residence_country': [u'US'], u'invoice': [u'1-b1708259-bfbb-49c3-9886-c8d376449610'], u'payer_status': [u'verified'], u'txn_type':[u'web_accept'], u'handling_amount': [u'0.00'], u'payment_date': [u'07:14:24 Aug 17, 2015 PDT'], u'first_name': [u'Mike'],u'item_name': [u'Cheese'], u'charset': [u'utf-8'], u'custom': [u''], u'notify_version': [u'3.8'], u'transaction_subject': [u''],u'test_ipn': [u'1'], u'item_number': [u''], u'receiver_id': [u'9HXLXHFWVDHMY'], u'business': [u'merchant@somesite.com'], u'payer_id':[u'U4KRAKEBX54K4'], u'auth': [u'AyTr4qaCrPAlUt2bb3Vq8WoF4cnWkZGxqs4NhXm1wcohCDHd-xXTClihy3V14nnXqVlL0o3-TCjS8goMPWF8yrQ'],u'verify_sign': [u'An5ns1Kso7MWUdW4ErQKJJJ4qi4-AGEN-sbiMEvw1zwTlDjlqN.0DXZo'], u'payment_fee': [u'0.37'], u'mc_fee': [u'0.37'],u'mc_currency': [u'USD'], u'shipping': [u'0.00'], u'payer_email': [u'humpty@dumpty.com'], u'payment_type': [u'instant'], u'mc_gross':[u'2.30'], u'quantity': [u'1']}>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As you can see, PayPal posts back the info and we can see quite a lot from this.

`payment_status` shows us what we need to know the most though, and as you can
see, it says ‘Completed’ in our sample. As long as we get that response, we can
be sure to let our customers access the product.

### SUMMARY

As you can see, PayPal payments can be a complicated thing to manage, even at
the basic level. Consequently, there are a few places where you could fall into
difficulties.

The main points to remember are:

-   Create your testing accounts for buyer and merchant

-   Install the Django-Paypal module

-   Create your product buttons using the PayPalPaymentsForm

-   Remember to process the returned post information
