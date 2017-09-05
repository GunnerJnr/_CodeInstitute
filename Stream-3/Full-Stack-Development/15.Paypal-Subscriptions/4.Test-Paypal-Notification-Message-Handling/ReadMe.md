### TEST PAYPAL NOTIFICATION MESSAGE HANDLING

So now that we’ve written our code, we’re faced with a difficult situation, as
the *PayPal Instant Payment Notifications* (IPN) can only be sent to an internet
facing server, while regular home and corporate internet setups don’t allow for
arbitrary incoming connections.

To solve this, we can use an excellent command line tool that will forward
specific traffic from the internet to our development computer, thus allowing us
to pretend that we *are* an internet facing server!

[Ngrok](https://ngrok.com/) offers what is called a ‘secure tunnel to
localhost’, which means it allows internet traffic to reach your local
development machine just like it was a server on the internet.

If you click the *Download* button on the Ngrok homepage, you can download
versions for all platforms. You’ll find only one thing in the downloaded zip
file; a binary file called *ngrok*.

Save this file into the root **we_are_social** project folder, as we’re going to
be running this on the machine that will run your project.

 

### NOTE

This still applies even if you’re running this on a VM, as all traffic needs to
be sent to your VMS webserver.

 

You can start ngrok by typing: `ngrok http 8000` if using **cmd**, or `./ngrok
http 8000` if using **bash**or any other shell (the **./** is a way of
specifying the current directory).

This will establish a connection to the outside world and pass everything back
to your localhost, or 127.0.0.1 on port 8000, which is the same as the IP and
port that the Django development server runs on.

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/01/1452184082_image2.png)

  
As you can see, the http and https traffic is being forwarded from an external
web address to our localhost:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Forwarding                http://YOUR_NGROK_SUBDOMAIN.ngrok.io  -> localhost:8000                                                                                                        
Forwarding                https://YOUR_NGROK_SUBDOMAIN.ngrok.io -> localhost:8000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  
The url for http is the one we’re interested in, as we need to substitute our
settings.py PAYPAL_NOTIFY_URL with this new URL while we’re testing and add the
hostname (just the part after `//`) to the ALLOWED_HOSTS:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
PAYPAL_NOTIFY_URL = 'http://YOUR_NGROK_SUBDOMAIN.ngrok.io/a-very-hard-to-guess-url/'
...
ALLOWED_HOSTS = ['127.0.0.1','YOUR_NGROK_SUBDOMAIN.ngrok.io']
...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we run our development server, our *Subscribe* buttons will now contain the
alternative URL, and when we complete the process, an IPN will be sent to that
URL and passed back to our local development machine’s handlers in our
magazines/models.py.

 

### SUMMARY

As you can see, PayPal Subscriptions can be a lot to take in and manage as a
developer.

PayPal is a very secure and reliable payment gateway that many online customers
trust, so it’s worth your while to get to grips with its individual ways of
doing things.

And trust us, once you’ve done this a couple of times, it will feel like second
nature!
