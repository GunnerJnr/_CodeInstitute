angular.module('formControllers', [])
    .controller('FormController', function ($scope) {
        $scope.register = {};
        $scope.submitted = false;

        $scope.submit = function (myForm) {
            if (myForm.$valid) {
                $scope.submitted = true;
                // continue with form processing
                alert("Form Valid: " + $scope.register.username + " " + $scope.register.email);
                $scope.register = {}; //reset the form
                return; // return from function
            } else {
                alert("form is invalid")
            }

            $scope.submitted = true;
        };
    })
    .controller('SelectionController', function ($scope) {
        $scope.items = [{
                name: 'one',
                age: 30
        },
            {
                name: 'two',
                age: 27
        },
            {
                name: 'three',
                age: 50
        }];
        $scope.cars = ['mini', 'ferrari', 'bmw', 'VW'];

        $scope.wasSubmitted = false;
        $scope.selectedItem = $scope.items[0];

        $scope.selectedCar = $scope.cars[1];

        // for check box 
        $scope.checkboxModel = {
            fishing: true,
            golf: true,
            sailing: false,
            vote: 'down'
        };

        // for radio button
        $scope.color = {
            name: 'blue'
        };

        $scope.specialValue = {
            "id": "12345",
            "value": "green"
        };

        $scope.submit = function () {
            if ($scope.selectionForm.$valid) {
                $scope.wasSubmitted = true;
                alert("selected car: " + $scope.selectedCar);
                alert("selected item: " + $scope.selectedItem.name + " " + $scope.selectedItem.age);
            } else {
                alert("form is invalid")
            }
        };
    })
    .controller('RegisterController', function ($scope) {
        $scope.register = {};
        $scope.submitted = false;
        $scope.uniqueusername = true;
        $scope.uniqueemail = true;

        $scope.registerForm = function (registerForm) {
            if (registerForm.$valid) {
                $scope.submitted = true;
                // continue with form processing
                // use a service to check for validity of username
                $scope.uniqueusername = false;
                // use a service to check for validity of email
                $scope.uniqueemail = true;

                if ($scope.uniqueusername &&
                    $scope.uniqueemail) {
                    // proceed to process form via backend service
                    // if successful route to next page
                }
            } else {
                console.log("form is invalid");
                $scope.submitted = true;
            }
        };
    });