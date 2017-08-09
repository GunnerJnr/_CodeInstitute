angular.module('movieDBServices', []).factory('MovieListService', function ($http) {
    //    
    myServiceObj = {
        name: 'Movie Service',
        createdBy: 'Sean',
        getList: function (url) {
            return $http.get(url);
        }
    }
    return myServiceObj;
});