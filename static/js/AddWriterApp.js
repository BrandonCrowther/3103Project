angular.module('AddWriterApp', [])
	  			.controller('AddWriterController', ['$scope', '$http', function($scope, $http) {	
		 		 	$scope.addWriter = function (writer){
		 		 		console.log("hello world: " +JSON.stringify(writer));
		 		 	}
				}]);