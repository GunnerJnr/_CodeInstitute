CHALLENGE
=========

 

-   Make these changes and change the ng-controller value in index.html  to use
    the new controller.

-   Copy a package.json file from another project as we will need to run a local
    server.

-   make sure you have no local servers running in another command tool. Do a
    control+c in the command tool to stop one if running.

-   cd in a command tools and run \>npm start

-   navigate to localhost:8000

 

*index.html*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<!doctype html>
<html ng-app='<myAppName>'>
  <head>
        <title>Angular $http example</title>
    <script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>
 </head>
 <body>
 <div ng-controller='<myControllerName>'>
 *****your content*****
</div>
 </body>
  <script src='javascript/app.js'></script>
  <script src='javascript/controller.js'></script>
  <script src='javascript/service.js'></script>
</html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

What happens if there is an error?

 

Deliberately create a typo in the url of the \$http.get(url), i.e. misspell
‘student.json’. Use the debugger console to see what happens. Then add something
to the index.html file to indicate there is a problem.

 

Note to view this example you will need to open a command window in the root
folder and run ‘npm start’ this will install the node\_modules folder which will
in turn run a local mini server allowing us to view and test our angular js app.
