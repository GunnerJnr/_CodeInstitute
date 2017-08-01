// define our application
// We’ve passed an empty array to it. This array generally contains dependent modules,
// e.g. controllers, services, and directives, both builtin and custom.
angular.module("mainApp", ['myControllers']);

//------------------------------------------------------------------------------------//

/*
	We can refer to our application module, once defined, by referencing:
	angular.module("mainApp");   // note we’ve dropped the array definition
	We can use this reference to add controller, service and directive modules.
*/

//------------------------------------------------------------------------------------//

/*
	Defines our application and allows us to use built in functions, services and directives of the Angular framework as well as custom built functions, services, and directives. The application module is injected with dependencies to define the application. 
*/