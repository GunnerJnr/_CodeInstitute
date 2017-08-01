$(document).ready(function(){
    // declare out array of images
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

    // calculate a random image from our array
    var randomBackgroundImg = imgArray[Math.floor(Math.random() * imgArray.length)];

    // point to the image directory
    var imgPath = 'static/img/';

    // call on the dom to change the background element using the array
    document.body.style.backgroundImage = "url('"+imgPath+randomBackgroundImg+"')";
}); 