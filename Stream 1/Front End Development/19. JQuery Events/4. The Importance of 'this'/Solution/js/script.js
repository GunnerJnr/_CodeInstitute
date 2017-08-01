// wait until the doc is ready
$(document).ready(function () {
	$(".stream-nav").on("click", function () {
		// When we click on a 'box' class, this will run
		var elementId = $(this).attr("id"),
			cardClass = $(".card").attr("class").split(" ")[0];

		if ($("." + elementId).css("background-color") === "rgb(235, 82, 85)") {
			$("." + elementId).css("background-color", "#fff");
		} else {
			$("." + cardClass).css("background-color", "#fff");
			$("." + elementId).css("background-color", "rgb(235, 82, 85)");
		}
	});
});