angular.module('AddSeriesApp', [])
	.controller('AddSeriesController', ['$scope', '$http', function($scope, $http) {	
  		$scope.series_message = "";
  		$scope.publishers = function(){
			$http({
				method: 'GET',
				url: urlFor("/publishers"),
				data: {}
			}).success(function (result) {
				$scope.body = result;
			});
		}
		$scope.addSeries = function (series){
			$http({
				method = 'POST', 
				url = urlFor("/series"),
				data: series
			}).success(function (){
				$scope.series_message = "SUCCESS!!"
			}
		}
}]);
