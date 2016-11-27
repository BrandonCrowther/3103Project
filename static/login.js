$(function(){
	console.log("China");
});


function login(){
	var name = $('#username').val();
	var password = $('#password').val();

	$.ajax({
		url: "/login",
		data: {username: name, password: password},
		dataType: "json",
		type: "POST",
		success: function(){
			window.alert("You are successfully logged in as " + name);
		},
		failure: function(data){
			window.alert("Something went wrong logging in");
			console.log(data);
		}
	});
}
