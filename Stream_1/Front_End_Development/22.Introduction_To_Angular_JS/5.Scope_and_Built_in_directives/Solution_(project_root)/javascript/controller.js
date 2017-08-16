// create our controller module
angular.module('myControllers', []);

angular.module('myControllers').controller('MyController', function ($scope) {

	// set scope with first and last names
	$scope.firstName = "David";
	$scope.lastName = "Gunner Jnr";

	// & set a greetings function to the scope
	$scope.greeting = function () {
		return "Greetings " + $scope.firstName + " " + $scope.lastName;
	};
});

// NOTE:
// Naming convention: When we name modules, we usually use camel-case convention,
// i.e. lower case first word, capitalized subsequent words. 
// When naming controllers, we use all capitalized words.

// add another controller
angular.module('myControllers').controller('MyOtherController', function ($scope) {
	$scope.student = {
		firstName: " ",
		lastName: " "
	};
});

//----------------------------- Add More Controllers -------------------------------------//

/*
// add additional controllers by using the ‘chaining’ method,
// note the dropping of the ; at then end of the definition of ‘MyController’
.controller('MyOtherController', function ($scope) {
    // my other controller logic here
});
*/

//----------------------------- Another Approach -------------------------------------//

// Another approach is to define our controller module and then use references to it:
/*
angular.module('myControllers',[]);
 
angular.module('myControllers').controller('MyController',function($scope) {
// controller logic here
});
 
angular.module('myControllers').controller('MyOtherController',function($scope) {
// my other controller logic here
});
*/

//------------------------------------------------------------------------------------//

/*
	Marshalls our model data for passing on to our HTML templates or View and responds to user interaction within the view, in essence maintaining the state of our ViewModel. The controller module can contain one or many controllers.
*/