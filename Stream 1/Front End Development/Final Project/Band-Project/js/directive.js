// create a directive for our app
angular.module('bandAppDirectives', [])
    .directive('imageCarousel', function () {
        return {
            restrict: "E",
            scope: true,
            templateUrl: "templates/directives/carousel.html"
        };
    })
    .directive('itunesSearch', function () {
        return {
            restrict: "E",
            scope: true,
            templateUrl: "templates/directives/itunes-search.html"
        };
    })