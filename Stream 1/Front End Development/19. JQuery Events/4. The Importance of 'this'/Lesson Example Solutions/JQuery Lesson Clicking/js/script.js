$(document).ready(function () {
    $(".box").on("click", function () {
        /** when we click an element that has a box class, the event will be fired.*/
        var classNames = $(this).attr("class").split(" ");
        // create a variable for each item in the array.
        // [0] will always be 'box'
        // [1] will be the box number that was clicked (e.g. 'one', 'two' or 'three')
        var boxClass = classNames[0];
        var className = classNames[1];
        if ($(this).css("background-color") == "rgb(255, 0, 0)") {
            // if this object is already red turn it black
            $("." + className).css("background-color", "#000");
        } else {
            // Else turn all elements with a box class black
            // and then change the color of all elements
            // with the same class name as the clicked element
            // to red
            $("." + boxClass).css("background-color", "#000");
            $("." + className).css("background-color", "red");
        }
    });
});