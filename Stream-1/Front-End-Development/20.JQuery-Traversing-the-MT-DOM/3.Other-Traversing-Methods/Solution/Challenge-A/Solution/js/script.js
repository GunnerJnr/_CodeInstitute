$(document).ready(function () {
    // put your code here

    /* when a colored panel is clicked, all panels vanish 
    $(".theButton").on("click", function () {
        $(".theButton").hide();
    });*/

    /* when a colored panel is clicked just that panel vanishes */
    $(".theButton").on("click", function () {
        $(this).hide();
    });

    /* when panel is clicked all siblings fade to 10% */
    $(".container").on("click", function () {
        $(".container").siblings().fadeTo("slow", 0.1);
    });

    /* when reset is clicked all panels revert to full opacity */
    $(".superButton").on("click", function () {
        $(".container").siblings().fadeTo("slow", 1);
    });

    /* when mouse hovers over a panel it turns black */
    $(".theButton").mouseenter(function () {
        $(this).addClass("highlightBlack");
    });

    /* when the mouse moves away the panel reverts back to previous colour */
    /* when mouse hovers over a panel it turns black */
    $(".theButton").mouseleave(function () {
        $(this).removeClass("highlightBlack");
    });
});