// create the module and name it mainApp
// also include ngRoute for all our routing needs
angular.module('formsApp', ['ngRoute','formControllers','formDirectives']);
// configure our routes
angular.module('formsApp').config(function($routeProvider) {
	$routeProvider
		// route for the form page
		.when('/', {
			templateUrl : 'templates/form.html',
			controller  : 'FormController'
		})
		.when('/register', {
			templateUrl : 'templates/registerForm.html',
			controller  : 'RegisterController'
		})
		.when('/selections', {
			templateUrl : 'templates/selectionForm.html',
			controller  : 'SelectionController'
		})
		.otherwise({redirectTo: '/'}); ;
});