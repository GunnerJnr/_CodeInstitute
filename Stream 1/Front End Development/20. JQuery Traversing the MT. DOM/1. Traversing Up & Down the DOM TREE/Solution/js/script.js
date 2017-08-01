// wait until page is ready
$(document).ready(function () {
	// sets the <a> tag inside a paragraph tag to the colour yellow  
	$("p").click(function () {
		// function that returns all of the <a> tags child elements that are in this paragraph
		$(this).children("a").css("background-color", "yellow");
	});
});