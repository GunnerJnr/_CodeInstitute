/**
 * Created by David Gunner (Jnr) on 01/08/2017.
 * Purpose: To load a random background image each time the page is loaded or refreshed.
 **/

// When the doc is ready we want to call our function
$(document).ready(function () {
    // Point to the image directory
    var imgPath = 'static/img/';

    // Declare our array of images
    var imgArray = [
        'avengers_0.jpg',
        'avengers_1.jpg',
        'avengers_2.jpg',
        'avengers_3.jpg',
        'avengers_4.jpg',
        'avengers_5.jpg',
        'avengers_6.jpg',
        'avengers_7.jpg',
        'avengers_8.jpg'
    ];

    // Here we calculate a random image from our array to display each time the page is loaded/refreshed
    var randomBackgroundImg = imgArray[Math.floor(Math.random() * imgArray.length)];

    // Call on the dom to change the background element randomly using the array we created
    document.body.style.backgroundImage = "url('" + imgPath + randomBackgroundImg + "')";
}); 