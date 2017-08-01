// create a new controller
angular.module('collegeControllers', []).controller('StudentController', function ($scope, StudentService) {

    // return the student greetings and full name of the student
    $scope.student = StudentService.getStudent();

    $scope.greeting = function () {
        return "Greetings " + $scope.student.fullName();
    };

});

angular.module('collegeControllers', []).controller('RemoteStudentController', function ($scope, RemoteStudentService) {
    // pulls the data from the json file
    $scope.student = {};

    RemoteStudentService.getStudent()
        .then(function (result) {
            //promise complete
            $scope.student = result.data;
        })
        // if error occurs getting data
        .catch(function (error) {
            console.log('error', error);
        });

    // returns greeting with student first and last name
    $scope.greeting = function () {
        return "Greetings " + $scope.student.firstName + " " + $scope.student.lastName;
    };

    // toggle button for showing and hiding results
    $scope.showResults = function () {
        return ($scope.results ? $scope.results = false : $scope.results = true);
    };

    // filter the grades to show only mark equal to A grade
    $scope.aGradeFilter = function (subject) {
        return (subject.marks > 74);
    };
});