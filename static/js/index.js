(function(angular){
	var app = angular.module('BaseApp', []);

	app.controller('BaseController', function($scope, $http, $sce) {

	});

  app.controller('SigninController', function($scope, $http, $sce) {
    $scope.message = "";
    $scope.signin = function (user){
		if(user != undefined){
<<<<<<< HEAD
	    credentials = JSON.stringify({"username": user.username, "password": user.password});
=======
	    credentials = JSON.stringify({"username": user.username, "password" || "": user.password || ""});
>>>>>>> refs/remotes/origin/master
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
<<<<<<< HEAD
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
=======
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
>>>>>>> refs/remotes/origin/master
	});
})(window.angular);
