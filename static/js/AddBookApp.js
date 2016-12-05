angular.module('AddBookApp', [])
	  			.controller('AddBookController', ['$scope', '$http', function($scope, $http) {	
	  				$scope.writers =[{"id":"1","first_name":"Scott","lastName":"Snyder"}];
		 		 	$scope.series = [{"id":"1", "name":"Batman"}];
		 		 	$scope.addComicBook = function (comic){
		 		 		console.log("hello world: " +JSON.stringify(comic));
		 		 	}
				}]);