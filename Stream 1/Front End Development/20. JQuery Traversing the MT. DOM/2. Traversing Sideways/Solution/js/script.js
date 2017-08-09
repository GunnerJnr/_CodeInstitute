$(document).ready(function() {
 
/*$("p").click(function(){
	$("p").css('background-color','red');
});*/
$("h2").mouseenter(function(){
	$(this).css('background-color','lightblue');
	$(this).css('font-size','20px');
});
/*$(".bottom_button").mouseenter(function(){
	$('body').css('background-color','black');
	 
});
$(".bottom_button").mouseout(function(){
	$('body').css('background-color','grey');
	 
});*/
$("#button1").mouseenter(function(){
	$(this).fadeTo(1000,0.5);
	 
});
$("#button1").mouseout(function(){
	$(this).fadeTo(1000,1);
	 
});
$("#button1").click(function(){
	$("#para1").slideToggle(1000);	 
});
$("p").click(function(){
	$(this).children('a').css('background-color','yellow');	 
});
$(".card_image").click(function(){
	$(this).next().children('p').slideDown();	 
});
$(".card").click(function(){
	$(this).toggleClass("highlight");	 
});
$("#select_btn").click(function(){
	$(".card:not(.highlight)").hide();	 
});
$("#all_btn").click(function(){
	$(".card").show();	 
});
$("h2").addClass("underline");
   $("nav").addClass("border");
 	$("#stream1_btn").on("click", function() {
 		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream1").addClass('highlight_stream');
	});
	$("#stream2_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream2").addClass('highlight_stream');
	});
	$("#stream3_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
	  	$(".stream3").addClass('highlight_stream');
	});


}); 
