$(document).ready(function () {
    $("#stream1_btn").on("click", function () {
        $(".stream1").removeClass('highlight_stream');
        $(".stream2").removeClass('highlight_stream');
        $(".stream3").removeClass('highlight_stream');
        $(".stream1").addClass('highlight_stream');
    });
    $("#stream2_btn").on("click", function () {
        $(".stream1").removeClass('highlight_stream');
        $(".stream2").removeClass('highlight_stream');
        $(".stream3").removeClass('highlight_stream');
        $(".stream2").addClass('highlight_stream');
    });
    $("#stream3_btn").on("click", function () {
        $(".stream1").removeClass('highlight_stream');
        $(".stream2").removeClass('highlight_stream');
        $(".stream3").removeClass('highlight_stream');
        $(".stream3").addClass('highlight_stream');
    });
    $("p").on("click", function () {
        $("p").addClass("highlight-p");
    });
    $("h2").mouseenter(function () {
        $("h2").addClass("highlight-h2");
    });
    $("h2").mouseleave(function () {
        $("h2").removeClass("highlight-h2");
    });
    /*this will apply larger font size to the active h2 element 
     by adding the h2_font_size class but 
     not the other h2 elements by removing class h2_font_size from them*/

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
    $(".bottom_button").mouseenter(function () {
        $("body").addClass("highlight-bg");
    });
    $(".bottom_button").mouseleave(function () {
        $("body").addClass("unhighlight-bg");
    });

    $("#button1").click(function () {
        $("#button1").hide("slow");
    });
    $("#button2").click(function () {
        $("#toggle-p2").toggle("slow");
    });
    $("#button3").click(function () {
        $("#toggle-p3").slideToggle("fast");
    });
    //adds fade to when  mouserenter and mouseleave button
    $("#button4").mouseenter(function () {
        $('#button4').fadeTo(1000, .5);
    });
    $("#button4").mouseleave(function () {
        $('#button4').fadeTo(1000, 1);
    });
    //adds fade to when  mouserenter and mouseleave button
    $("#button5").mouseenter(function () {
        $('img').fadeTo(1000, .5);
    });
    $("#button5").mouseleave(function () {
        $('img').fadeTo(1000, 1);
    });
});