$(document).ready(function () {
    // put your code here

    /* display the rgb value in the reset button, of the selected panel */
    $(".theButton").on("click", function () {
        var selectedColor = $(this).css("background-color");
        $(".superButton").text("The selected panel colour is : " + selectedColor);
    });
});