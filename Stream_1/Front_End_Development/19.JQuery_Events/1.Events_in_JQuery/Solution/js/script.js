// when the document is ready
$(document).ready(function () {
	// this applies the colour red to the paragraphs when thay have been clicked on
	$("p").click(function () {
		$("p").addClass("highlight_text");
	});

	// this will add a lightblue colour to h2 elements
	$("h2").hover(function () {
		$("h2").addClass("highlight-h2");
	});

	/* 
		this will apply larger font size to the active h2 element by adding the h2_font_size class but 
	 	not the other h2 elements by removing class h2_font_size from them
	*/

	$("#hr_html").hover(function () {
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_python").removeClass("h2_font_size");
		$("#hr_jquery").removeClass("h2_font_size");
		$("#hr_django").removeClass("h2_font_size");
		$("#hr_css").removeClass("h2_font_size");
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_html").addClass("h2_font_size");

	});

	$("#hr_mysql").hover(function () {
		$("#hr_python").removeClass("h2_font_size");
		$("#hr_jquery").removeClass("h2_font_size");
		$("#hr_django").removeClass("h2_font_size");
		$("#hr_css").removeClass("h2_font_size");
		$("#hr_html").removeClass("h2_font_size");
		$("#hr_mysql").addClass("h2_font_size");

	});

	$("#hr_python").hover(function () {
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_jquery").removeClass("h2_font_size");
		$("#hr_django").removeClass("h2_font_size");
		$("#hr_css").removeClass("h2_font_size");
		$("#hr_html").removeClass("h2_font_size");
		$("#hr_python").addClass("h2_font_size");

	});

	$("#hr_jquery").hover(function () {
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_python").removeClass("h2_font_size");
		$("#hr_django").removeClass("h2_font_size");
		$("#hr_css").removeClass("h2_font_size");
		$("#hr_html").removeClass("h2_font_size");
		$("#hr_jquery").addClass("h2_font_size");

	});

	$("#hr_django").hover(function () {
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_python").removeClass("h2_font_size");
		$("#hr_jquery").removeClass("h2_font_size");
		$("#hr_css").removeClass("h2_font_size");
		$("#hr_html").removeClass("h2_font_size");
		$("#hr_django").addClass("h2_font_size");

	});

	$("#hr_css").hover(function () {
		$("#hr_mysql").removeClass("h2_font_size");
		$("#hr_python").removeClass("h2_font_size");
		$("#hr_jquery").removeClass("h2_font_size");
		$("#hr_django").removeClass("h2_font_size");
		$("#hr_html").removeClass("h2_font_size");
		$("#hr_css").addClass("h2_font_size");

	});

	//applys colour black to body  background when mouseenter over buttons
	$(".bottom_button").mouseenter(function () {
		$("body").css("background-color", "black");

	});

	//applys colour grey to body background wneh mouseleaves buttons
	$(".bottom_button").mouseleave(function () {
		$("body").css("background-color", "#eee");
	});
});