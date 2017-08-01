// create a new controller
angular.module('collegeControllers', []).controller('StudentController', function ($scope, StudentService) {

    // return the student greetings and full name of the student
    $scope.student = StudentService.getStudent();
    $scope.greeting = function () {
        return "Greetings " + $scope.student.fullName();
    };

    //for the toggle effect on buttons 
    $scope.showResults = function () {
        return ($scope.results ? $scope.results = false : $scope.results = true);
    };
});