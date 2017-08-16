// wait until the doc is ready
$(document).ready(function () {
	// removes the claas makeRed, and adds the class makeBorder on mouseenter
	$("button").mouseenter(function () {
		$(this).removeClass("makeRed").addClass("makeBorder");

	});

	// does the opposite to the above on the mouseleave
	$("button").mouseleave(function () {
		$("button").removeClass("makeBorder").addClass("makeRed");

	});

	// toggles paragraphs when either button is clicked
	$("button").click(function () {
		$("p").slideToggle(3000);
	});

	// hides/shows  paragraphs when either button is clicked
	$("button").click(function () {
		$("p").hide(1500).show(2500);
	});

	// fadeIn and fadoeOut on paragraphs when either button is clicked
	$("button").click(function () {
		$("p").fadeIn().fadeOut();
	});


});