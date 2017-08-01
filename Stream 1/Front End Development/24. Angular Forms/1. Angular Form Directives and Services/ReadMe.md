CHALLENGE
=========

 

**Challenge A:**

Using the `jsfiddle` example above add some additional error checking.

 

Add a validation to the age field so that age can only be only be a number.  Add
some debug to see if it working. We are using a regular expression here, which
is a topic we won’t cover in depth in these lessons but is worth spending some
time exploring.

 

**Challenge B:**

We have our validations set up, so now we want to display some error messages on
the form if we have invalid data.

 

Let’s add the following after the username input once we’ve gone through the
details (after the `<div>` inside the row `<div>` )

 

Note that the errors only show after the form has been submitted. You can change
this by removing the `&&submitted` condition.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="col-md-5 error-container" ng-show="register_form.username.$dirty 
    && register_form.username.$invalid                             && submitted">
   <label style='color: red'>Error:</label>
    <p class="error"  ng-show="register_form.username.$error.required">
             Please input a username</p>
    <p class="error" ng-show="register_form.username.$error.minlength">
             Your username is required to be at least 3 characters</p>
    <p class="error" ng-show="register_form.username.$error.maxlength">
             Your username cannot be longer than 20 characters</p>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We are displaying error messages based on the error values of the form element
using the ng-show attribute. If there is an error then the error message will be
shown. We can see that there is an error value available for each of the
validation attributes.

 

Let’s add a similar error display for the email input field. Changing the error
messages and form input names appropriately.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="col-md-5 error-container" ng-show="
          register_form.email.$dirty
       && register_form.email.$invalid 
       && submitted">
       <label style='color: red'>Error:</label>
       <p class="error" ng-show="register_form.email.$error.required">
             Please input an email</p>
       <p class="error" ng-show="register_form.email.$error.minlength">
             Your email is required to be at least 5 characters</p>
       <p class="error" ng-show="register_form.email.$error.maxlength">
             Your email cannot be longer than 40 characters</p>
       <p class="error" ng-show="register_form.email.$error.email">
             That is not a valid email. Please input a valid email.</p>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Take a look at the `style.css` file. Change the values for `.ng-valid` and see
the effect. Add the class `.ng-invalid`with some styling.

 

If the submission is successful, add the following to the `formController` when
the form is valid:

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 $scope.submitted = false;
//continue with form processing
alert("Form Valid: " + $scope.register.username + " " +  $scope.register.email);
 $scope.register = {}; //reset the form
 return; // return from function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

NOTE:

We get an extra error option as we’ve used `type=’email’` on the input
field. For an updated version of the above, navigate to
`localhost:8000/#/register` in your browser.

Compare this page to the one you created. Enter some data and observe error
messages when submit button pressed.  

 

Note to view this example you will need to open a command window in the root
folder and run ‘npm start’ this will install the node\_modules folder which will
in turn run a local mini server allowing us to view and test our angular js app.
