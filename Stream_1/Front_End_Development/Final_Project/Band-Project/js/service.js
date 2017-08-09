angular.module('bandAppServices', []).factory('bandAppService', function ($http) {
	//   
	return {
		getList: getList
	};

	function getList(url) {
		return $http.get(url);
	}
});