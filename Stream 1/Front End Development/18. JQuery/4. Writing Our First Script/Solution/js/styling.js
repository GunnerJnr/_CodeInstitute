// wait until the document is ready
$(document).ready(function () {
	// add the css class to the odd table rows
	$("tr:odd").addClass("selection-odd");
	$("tr:even").addClass("selection-even");
});