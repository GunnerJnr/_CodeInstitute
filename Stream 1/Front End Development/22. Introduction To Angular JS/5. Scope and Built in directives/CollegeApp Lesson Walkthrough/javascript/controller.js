// create a new controller
angular.module('collegeControllers', []).controller('StudentController', function ($scope) {

	// create a student array object
	var student = {
		firstName: "David",
		lastName: "Gunner Jnr",
		fees: 5000,
		subjects: [{
			name: "HTML",
			marks: 90
        }, {
			name: "CSS",
			marks: 85
        }, {
			name: "Javascript",
			marks: 70
        }, {
			name: "JQuery",
			marks: 82
        }, {
			name: "Angular JS",
			marks: 99
        }],

		// create a function to return the full name
		fullName: function () {
			return this.firstName + " " + this.lastName;
		}
	};

	//create greeting
	$scope.student = student;
	$scope.greeting = function () {
		return "Greetings " + $scope.student.fullName();
	};

	//for the toggle effect on buttons 
	$scope.showResults = function () {
		return ($scope.results ? $scope.results = false : $scope.results = true);
	};
});