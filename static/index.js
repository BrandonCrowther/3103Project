
function submitQuery(){
	var form_id = $("#form_selector").val()
	$.ajax({
		url: "/" + form_id,
		data: $("#" + form_id).serialize(),
		dataType: "json",
		type: "POST",
		success: function(data){
			$("#results").innerHTML(data);
		},
		failure: function(data){
			window.alert("Something went wrong. Check the console for information.");
			console.log(data);
		}
	});
}

function changeForm(){
	$('#form_holder form').hide();
	$("#form_holder #" + $("#form_selector").val()).show();
}
