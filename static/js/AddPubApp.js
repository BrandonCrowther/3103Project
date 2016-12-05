angular.module('AddPubApp', [])
	.controller('AddPubController', ['$scope', '$http', function($scope, $http) {	
		$scope.addPublisher = function (publisher){
			console.log("hello world: " +JSON.stringify(publisher));
		}
}]);
