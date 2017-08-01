CHALLENGE
=========

 

**Part A:**

Add the greeting to the html view.

**Part B:**

Incorporate ng-hide/ng-show in our example with some appropriate content, e.g.
“A Grades only”.

**Part C:**

The ng-click & ng-show example above shows and hides the students results. Add
another button and change the label on the existing one, so that we have two
buttons “Show Results” and “Hide Results”. When the “Show Results” button is
clicked the results are shown. But we now want to hide the “Show Results” button
and show the “Hide Results” button. The “Hide Results” button should hide the
results when clicked, hide the “Hide Results” button and show the “Show Results”
button, i.e. only one button should display at a time.

First step is to add a new \$scope variable and initialise it to true:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$scope.results = true;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note the function we call when the button is clicked:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$scope.showResults = function(){
 
  return ($scope.results ? $scope.results=false : $scope.results=true)
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function essentially ‘toggles’ the value of \$scope.results. If you are not
familiar with the code in the return statement, it is using a Javascript ‘idiom’
which is shorthand for:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if ($scope.results)
      return $scope.results = false
else
      return $scope.results = true
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
