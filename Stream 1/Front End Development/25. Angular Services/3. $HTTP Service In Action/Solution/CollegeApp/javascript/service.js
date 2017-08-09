// create our service
angular.module('collegeServices', []).factory('StudentService', function () {
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
            // create and initialise an object to store student
            var studentObj;
            studentObj = student;
            return studentObj.firstName + " " + studentObj.lastName;
        }
    };

    // return the student object
    return {
        getStudent: function () {
            return student;
        }
    };
});

angular.module('collegeServices', []).factory('RemoteStudentService', function ($http) {
    // return Student Service
    return {
        getStudent: getStudent
    };

    function getStudent() {
        return $http.get('student.json'); // returns a promise
    }
});