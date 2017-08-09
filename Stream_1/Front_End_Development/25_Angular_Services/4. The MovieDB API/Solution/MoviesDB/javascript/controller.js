angular.module('movieDBControllers', [])
    .controller('MovieListController', function ($scope, MovieListService) {
        // create our url with our api key
        var url = "https://api.themoviedb.org/3/movie/popular?api_key=8ce4b1e8a499c784a9fce364f1a41c47";

        $scope.movieList = [];

        MovieListService.getList(url).then(function (result) {
            $scope.movieList = result.data.results;
        }).catch(function (error) {
            console.log('error', error);
        });
    });