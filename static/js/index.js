(function(angular){
	var app = angular.module('BaseApp', []);

	app.directive('includeReplace', function () {
		return {
			require: 'ngInclude',
			restrict: 'A', /* optional */
			link: function (scope, el, attrs) {
				el.replaceWith(el.children());
			}
		};
	});

	app.filter("trust", ['$sce', function($sce) {
		return function(htmlCode){
			return $sce.trustAsHtml(htmlCode);
		}}]
	); //remove later

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
				location.reload();
			}).error(function(result){
				location.reload();
			});
		}
	});

	app.controller('SigninController', function($scope, $http, $sce) {
		$scope.signIn = function (user){
			if(user != undefined){
				if(user.username != undefined && user.password != undefined){
					credentials = JSON.stringify({"username": user.username, "password": user.password});
					$http({ //successfully sign in
						method: 'POST',
						url: urlFor("/signin"),
						data: credentials
					}).success(function (result) {
						$http({ //re-render the index page here
							method: 'GET',
							url: urlFor("/validate_login"),
							data: {}
						}).success(function (result) {
							location.reload();
						});
					});
				}
			}
		}
	});

	app.controller('GetController', function($scope, $http, $sce) {
		$scope.publishers =  [];
		$scope.writers = [];
		$scope.series = [];
		$scope.comics = [];

		$http({
			method: 'GET',
			url: urlFor("/publishers"),
			data: {}
		}).success(function (result) {
			$scope.publishers = result.result;
		});
		$http({
			method: 'GET',
			url: urlFor("/writers"),
			data: {}
		}).success(function (result) {
			$scope.writers = result.result;
		});
		$http({
			method: 'GET',
			url: urlFor("/series"),
			data: {}
		}).success(function (result) {
			$scope.series = result.result;
		});

		$scope.viewAll = function(){
			$http({
				method: 'GET',
				url: urlFor("/comics"),
				data: {}
			}).success(function (result) {
				$scope.comics = result.result;
			});
		}
		$scope.forPublisher = function(){
			$http({
				method: 'GET',
				url: urlFor("/comic/publisher/" + $scope.publisher),
				data: {}
			}).success(function (result) {
				$scope.comics = result.result;
				console.log(result);
			});
		}
		$scope.forWriter = function(){
			$http({
				method: 'GET',
				url: urlFor("/comic/writer/" + $scope.writer),
				data: {}
			}).success(function (result) {
				$scope.comics = result.result;
			});
		}
		$scope.forSeries = function(){
			$http({
				method: 'GET',
				url: urlFor("/comics"),
				data: {}
			}).success(function (result) {
				$scope.comics = result.result;
			});
		}

	});
})(window.angular);
