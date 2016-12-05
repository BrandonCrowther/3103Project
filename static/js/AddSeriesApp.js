angular.module('AddSeriesApp', [])
	.controller('AddSeriesController', ['$scope', '$http', function($scope, $http) {	
  		$scope.publishers = [{"id":"1","name":"DC"}, {"id":"2","name":"Marvel"}];
		$scope.addSeries = function (series){
			console.log("hello world: " +JSON.stringify(series));
		}
}]);
