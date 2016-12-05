angular.module('AddBookApp', [])
	.controller('AddBookController', ['$scope', '$http', function($scope, $http) {	
		$scope.book_message = "";
		$scope.writers = function(){
			$http({
				method: 'GET',
				url: urlFor("/writers"),
				data: {}
			}).success(function (result) {
				$scope.body = result;
			});
		}
		$scope.series = function(){
			$http({
				method: 'GET',
				url: urlFor("/publishers"),
				data: {}
			}).success(function (result) {
				$scope.body = result;
			});
		}
		$scope.addComicBook = function (comic){
			$http({
				method = 'POST', 
				url = urlFor("/comic"),
				data: comic
			}).success(function (){
				$scope.book_message = "SUCCESS!!"
			}
		
	}
}]);