(function(angular){
	var app = angular.module('BaseApp', []);

	app.filter("trust", ['$sce', function($sce) {
		return function(htmlCode){
			return $sce.trustAsHtml(htmlCode);
		}}]
	);

	app.controller('BaseController', function($scope, $http, $sce) {
		$http({
			method: 'GET',
			url: urlFor("/validate_login"),
			data: {}
		}).success(function (result) {
			$scope.body = result
		});

		$scope.logout = function(){
			$http({
				method: 'DELETE',
				url: urlFor("/login"),
				data: {}
			}).success(function (result) {
				$scope.body = result;
			});
		}
	});

	app.controller('SigninController', function($scope, $http, $sce) {
		$scope.signin = function (user){
			if(user != undefined){
				if(user.username != undefined && user.password != undefined){
					credentials = JSON.stringify({"username": user.username, "password": user.password});
					$http({ //successfully sign in
						method: 'POST',
						url: urlFor("/signin"),
						data: {}
					}).success(function (result) {
						$http({ //re-render the index page here
							method: 'GET',
							url: urlFor("/validate_login"),
							data: {}
						}).success(function (result) {
							$scope.self = result
						});
					});
				}
			}
		}
	});

	app.controller('GetController', function($scope, $http, $sce) {
		$scope.publishers =  [];
		$scope.writers = [];
		$scope.series = []
		$http({
			method: 'GET',
			url: urlFor("/publishers"),
			data: {}
		}).success(function (result) {
			//$scope.publishers = result;
		});
		$http({
			method: 'GET',
			url: urlFor("/writers"),
			data: {}
		}).success(function (result) {
			//$scope.publishers = result;
		});
		$http({
			method: 'GET',
			url: urlFor("/series"),
			data: {}
		}).success(function (result) {
			//$scope.publishers = result;
		});

		$scope.viewAll = function(){
			$http({
				method: 'GET',
				url: urlFor("/comics"),
				data: {}
			}).success(function (result) {
				$scope.content = "Success";
			});
		}
		$scope.forPublisher = function(){
			$http({
				method: 'GET',
				url: urlFor("/comic/publisher/" + $scope.publisher),
				data: {}
			}).success(function (result) {
				$scope.content = "Success";
			});
		}
		$scope.forWriter = function(){
			$http({
				method: 'GET',
				url: urlFor("/comic/writer/" + $scope.writer),
				data: {}
			}).success(function (result) {
				$scope.content = "Success";
			});
		}
		$scope.forSeries = function(){
			$http({
				method: 'GET',
				url: urlFor("/comics"),
				data: {}
			}).success(function (result) {
				$scope.content = "Success";
			});
		}

	});
})(window.angular);
