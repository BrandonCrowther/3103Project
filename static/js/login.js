angular.module('SigninApp', [])
  .controller('SigninController', ['$scope', '$http', function($scope, $http) {
    $scope.message = "";
    $scope.signin = function (user){
      credentials = JSON.stringify({"username": user.username, "password": user.password});
     $http.post(urlFor("/signin"), credentials ).then(function(data) {
        if(data.status == 201) {
          $scope.message = "You are now successfully logged in as " + data.username + "."
       }
       else{
         $scope.message = "Invalid credentials."
       }
    });
}}]);
