// We’ve added ‘ngRoute’ as a dependency in our application setup.
angular.module('routingApp', ['ngRoute', 'routingControllers']);

// configure our routes
// We’ve attached the config function to our application where we’ve passed the built-in service 
// $routeProvider as a parameter to the config function which allows us to define our routing
angular.module('routingApp').config(function ($routeProvider) {
	// The $routeProvider service provides a function when() which takes as parameters
	$routeProvider
	// route for the home page
		.when('/', { // route path
			templateUrl: 'templates/home.html', // the template html file
			controller: 'HomeController' // controller to associate with the templateURL file
		})
		// route for the about page
		.when('/about', { // route path
			templateUrl: 'templates/about.html', // the template html file
			controller: 'AboutController' // controller to associate with the templateURL file
		})
		// route for the contact page 
		.when('/contact', { // route path
			templateUrl: 'templates/contact.html', // the template html file
			controller: 'ContactController' // controller to associate with the templateURL file
		})
		// add our details page
		.when('/details/:page', {
			templateUrl: 'templates/details.html',
			controller: 'DetailsController'
		})
		// otherwise redirect to ..
		.otherwise({
			redirectTo: '/' // route path
		}); // if not above path
});

/* NOTE:
	For each new route, we attach a .when() function to the $routeProvider service passing as parameters

	the route
	the template html file
	and the associated controller
*/

/* NOTE: 
	We have created separate html templates for each page of our application and moved them to a templates folder. You will note that we have assigned a controller to each template. This means that we can dispense with the ng-controller attribute we have used up to now. Although we can still use this method if a portion of our template needs an additional controller assigned to it.
	
	Also remember that because our html templates are injected into our ‘shell’ html file (usually index.html), we don’t need to include any Javascript files (e.g. angular framework files) or css files in these templates, as the files have already been included in the index.html. This is unless there is a specific file that the html template requires on its own.
*/