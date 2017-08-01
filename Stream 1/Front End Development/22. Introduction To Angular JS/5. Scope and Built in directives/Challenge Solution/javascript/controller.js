// create a new controller
angular.module('collegeControllers', []).controller('StudentController', function ($scope) {

	// create and store results and initialise results to true
	$scope.results = true;

	// create a student array and fill in some properties for the data to display
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
			var studentFullName = student; // store the students name value

			// store and return the full name
			return studentFullName.firstName + " " + studentFullName.lastName;
		}
	};

	$scope.student = student; // set student

	//create greeting function
	$scope.greeting = function () {
		// return the full name of the student
		return "Greetings " + $scope.student.fullName();
	};

	// create a toggle function for the buttons
	$scope.showResults = function () {
		$scope.results = false;
	};

	//
	$scope.hideResults = function () {
		$scope.results = true;
	};
});