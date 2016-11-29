(function(angular){
	var app = angular.module('BaseApp', []);

	app.controller('BaseController', function($scope, $http, $sce) {

	});

  app.controller('SigninController', function($scope, $http, $sce) {
    $scope.message = "";
    $scope.signin = function (user){
		if(user != undefined){
	    credentials = JSON.stringify({"username": user.username, "password" || "": user.password || ""});
	    $http.post(urlFor("/signin"), credentials ).then(
				function successCallback(data) {
					$scope.message = "You are now successfully logged in as " + data.username + "."
				},
				function errorCallback(data){
					$scope.message = "Invalid credentials."
				}
	    );
		}
	}});

	app.controller('GetController', function($scope, $http, $sce) {
		$scope.viewAll = function(){
			$http.get(urlFor("/comics"), JSON.stringify({})).then(
				function successCallback(data) {
					$scope.body = "Working route"
				},
				function errorCallback(data){
					$scope.body = "Oops I fucked up."
				}
	    );
		}
	});
})(window.angular);
