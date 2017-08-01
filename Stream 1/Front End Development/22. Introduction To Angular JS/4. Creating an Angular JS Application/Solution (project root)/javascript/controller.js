// create our controller module
angular.module('myControllers', []).controller('MyController', function ($scope) {
	// controller logic here
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