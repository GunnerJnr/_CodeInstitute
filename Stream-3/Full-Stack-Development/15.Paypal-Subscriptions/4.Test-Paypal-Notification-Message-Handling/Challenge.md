### CHALLENGE A

Add the ngrok URL to your PAYPAL_NOTIFY_URL and perform a successful
subscription and note what the recorded traffic looks like in your
terminal/console where you’re running ngrok.

Then check that the signal was caught and your purchase magazine purchase was
recorded.

 

### CHALLENGE B

Alter your settings.py to only use the ngrok URL when in DEBUG mode.

 

### CHALLENGE C

Import the ‘payment_was_successful’ signal, and see if you can work out what you
could do to extend the `subscription_end` value when a new monthly payment is
made.

 

### USEFUL RESOURCES

### ADDITIONAL PERSPECTIVES FROM PEOPLE WE LIKE

https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html

 

See `settings.py` in the lesson files for challenge solutions.
