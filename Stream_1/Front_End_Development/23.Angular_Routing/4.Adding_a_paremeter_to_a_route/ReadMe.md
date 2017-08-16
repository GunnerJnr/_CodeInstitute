CHALLENGE
=========

 

Let’s update our application to add a route with a parameter.

Let’s add the new route to the **app.js** file. Add the following,
before `.otherwise`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.when('/details/:page', {
            templateUrl : 'templates/details.html',
            controller  : 'DetailsController'
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We now need a new controller and template. The new Details controller will have
the **\$routeParams** service added to it. Inside the controller we will add a
title to the scope and retrieve the parameter and set it on a new scope
variable `wherefrom`. Add the new controller to the controller.js file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.controller('DetailsController',function($scope,$routeParams) {
      //
      $scope.title='Details Page';
      $scope.wherefrom=$routeParams.page;
 })
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Let’s create a new template in the templates folder called **details.html** so
that it looks like:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div>
  <h1>{{title}}</h1>
  <p>You came from {{wherefrom}} </p>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

To access this new details page, we should add a link to our existing pages. To
the **home**, **about**, and **contact**templates add the following link at the
end of the html:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<a href='#/details/{{title}}'>Go to details</a>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save your changes and reload your browser. Observe the changes. Make the link
look pretty if you have time (e.g. use a bootstrap button).

 

Note to view this example you will need to open a command window in the root
folder and run ‘npm start’ this will install the node\_modules folder which will
in turn run a local mini server allowing us to view and test our angular js app.
