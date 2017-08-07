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
            intro: "Click here to reload the dashboard at any time.",
            position: 'bottom-middle'
        },
        {
            element: '#step2',
            intro: 'You can also click here to reload the dashboard at any time also.',
            position: 'bottom-middle'
        },
        {
            element: '#year-menu-select',
            intro: 'This is a drop down list containing the years different Avengers were created/arrived. ' +
            'Selecting one will filter the data.',
            position: 'middle'
        },
        {
            element: '#name-menu-select',
            intro: 'This is a drop down list containing the names of the different Avengers. ' +
            'Selecting one will filter the data.',
            position: 'middle'
        },
        {
            element: '#url-menu-select',
            intro: 'This list contains urls where information can be found about the different characters, ' +
            'currently it will just filter the data.',
            position: 'middle'
        },
        {
            element: '#gender-row-chart',
            intro: 'Here you can see the percentage ratio of Male to Female characters, this can be filtered by clicking on either.',
            position: 'middle'
        },
        {
            element: '#honorary-pie-chart',
            intro: 'The pie chart contains all the honorary data for the different Avengers. This can be filtered by clicking the slices.',
            position: 'middle'
        },
        {
            element: '#years-nd',
            intro: 'Displays the total number of years.',
            position: 'middle'
        },
        {
            element: '#appearances-nd',
            intro: 'Displays the total number of Avenger appearances',
            position: 'middle'
        },
        {
            element: '#year-bar-chart',
            intro: 'Here is a bar chart displaying the years in a different way, you can drag the mouse over a selection to filter the data.',
            position: 'middle'
        },
        {
            element: '#current-bar-chart',
            intro: 'Here is a bar chart displaying the current Avengers, you can drag the mouse over a selection to filter the data.',
            position: 'middle'
        },
        {
            element: '#table-wrapper',
            intro: 'Below you can also view a table displaying different types of information about the named Avengers.',
            position: 'bottom-middle'
        }
    ]
});

$('#tour-button').click(function () {
    intro.start();
    $('#tour-button').hide();
});