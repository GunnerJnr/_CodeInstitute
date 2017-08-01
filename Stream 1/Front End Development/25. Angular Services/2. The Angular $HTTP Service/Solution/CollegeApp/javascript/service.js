// create our service
angular.module('ourServices', []).factory('OurPromise', function ($q, $timeout) {
    var getMessages = function () {
        var deferred = $q.defer(); // set up the promise here
        // referenced by deferred.promise
        // the function inside the timeoput gets executed after the delay 2000ms
        $timeout(function () {
            deferred.resolve({
                message: 'Its a Promise'
            }); // returns the results
        }, 2000);
        return deferred.promise; // return the promise object
    };
    return {
        getMessages: getMessages
    };
});