$(function(){
	console.log("China");
});


function login(){
	$.ajax({
		url: "/login",
		data: $('form').serialize(),
		dataType: "json",
		type: "POST",
		success: function(){
			window.alert("You are successfully logged in.");
		},
		failure: function(data){
			window.alert("Something went wrong logging in.");
			console.log(data);
		}
	});
}
