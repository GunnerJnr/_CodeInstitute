/**
 * Created by David Gunner (Jnr) on 03/08/2017.
 */

// create an instance of intro.js
var intro = introJs();

// next we want to set up our intro to the relevant elements
intro.setOptions({
    steps: [
        {
            element: '#step1',
            intro: "Click here to reload the dashboard",
            position: 'bottom-middle'
        },
        {
            element: '#step2',
            intro: 'Click here also to reload the dashboard',
            position: 'bottom-middle'
        },
        {
            element: '#year-menu-select',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#name-menu-select',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#url-menu-select',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#gender-row-chart',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#honorary-pie-chart',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#years-nd',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#appearances-nd',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#year-bar-chart',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#current-bar-chart',
            intro: 'TODO',
            position: 'middle'
        },
        {
            element: '#table-wrapper',
            intro: 'TODO',
            position: 'bottom-middle'
        }
    ]
});

$('#tour-button').click(function () {
    intro.start()
});