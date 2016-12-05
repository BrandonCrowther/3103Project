angular.module('AddWriterApp', [])
	.controller('AddWriterController', ['$scope', '$http', function($scope, $http) {	
	 	$scope.writer_message = "";
	 	$scope.addWriter = function (writer){
			$http({
				method = 'POST', 
				url = urlFor("/publishers"),
				data: writer
			}).success(function (){
				$scope.writer_message = "SUCCESS!!"
			}
	 	}
}]);