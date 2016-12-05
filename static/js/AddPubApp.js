angular.module('AddPubApp', [])
	.controller('AddPubController', ['$scope', '$http', function($scope, $http) {	
		$scope.pub_message = "";
		$scope.addPublisher = function (publisher){
			$http({
				method = 'POST', 
				url = urlFor("/publishers"),
				data: publisher
			}).success(function (){
				$scope.pub_message = "SUCCESS!!"
			}
		}
}]);
