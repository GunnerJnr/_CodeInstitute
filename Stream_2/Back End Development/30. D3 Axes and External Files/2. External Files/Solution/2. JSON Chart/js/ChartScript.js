// variables for the svg height, width and spacing between graph items
var svgWidth = 800;
var svgHeight = 600;
var spacing = 5;

// create and setup our canvas, this creates the margin settings
var margin = {
    top: 50,
    right: 0,
    bottom: 50,
    left: 50
};
// then we apply the margin to the canvas (width & height)
var canvasWidth = svgWidth + margin.right + margin.left;
var canvasHeight = svgHeight + margin.top + margin.bottom;

// access the data in a json file to output as bars in the chart
d3.json("json/list.json", function (error, myData) {
    myData.forEach(function (d) {
        d.username = d.user;
        d.score = +d.score; // the + here converts to a number
    });

    // create a variable to store the function for d3.max()
    var maxData = d3.max(myData, function (d) {
        return d.score;
    });

    // set up the scales for the height of the graph items in the chart
    var heightScale = d3.scale.linear()
        .domain([0, maxData])
        .range([0, svgHeight]); // -

    // set up colour for the scale
    var colorScale = d3.scale.linear()
        .domain([0, maxData])
        .range(["blue", "red"]);

    // append the div to add an id of tooltip
    var tooltip = d3.select("body")
        .append("div")
        .classed("hidden", true)
        .attr("id", "tooltip");

    // create a new yAxis scale with an inverted range
    var yAxisScale = d3.scale.linear()
        .domain([0, maxData])
        .range([svgHeight, 0]);

    // create our axis function
    var yAxis = d3.svg.axis()
        .scale(yAxisScale) // give it a scale
        .orient("left") // give it an orientation (left, top, bottom, or right)
        .ticks(11); // set the ticks to display on the axis (e.g 0, 5, 10, 20, 30, etc..)

    // set our svg properties
    var canvas = d3.select("body") // append svg to the body and set properties
        .append("svg")
        .attr("width", canvasWidth)
        .attr("height", canvasHeight)
        .attr("style", "background-color:#ddd"); // add some style

    canvas.append("g")
        .attr("class", "axis") // style axis vis css
        .attr("transform", "translate(" + (margin.left - 2) + "," + margin.bottom + ")")
        .call(yAxis);

    // call the yAxis function to generate the ticks, must be called at the end of our script 
    // (g = group) to ensure the axis is generated after the other elements in the svg and will
    // appear above them
    var svg = canvas.append("g")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
        .attr("style", "background-color:#ddd") // add some styling
        .attr("transform", "translate(" + margin.left + "," + margin.bottom + ")");

    //add code here
    svg.selectAll("rect")
        .data(myData)
        .enter()
        .append("rect")
        .attr("x", function (d, i) {
            return i * (svgWidth / myData.length);
        }) // multiply the index by the width
        .attr("y", function (d) {
            return svgHeight - (heightScale(d.score));
        }) // height is 300 (also we want to flip the graph as origin is top left, we also multiply by 5 to make the graph height bigger)
        .attr("width", (svgWidth / myData.length) - spacing) // keeps the scale
        .attr("height", function (d) {
            return (heightScale(d.score));
        }) // call an anonymous function
        .attr("fill", function (d) {
            return (colorScale(d.score));
        })
        .on("mouseover", function (d) {
            d3.select("#tooltip")
                .classed("hidden", false)
                .style("left", d3.event.pageX - 10 + "px") // in this case we need 
                .style("top", d3.event.pageY - 70 + "px") //to append px as units
            tooltip.html(d.score); // add an event which will trigger the Tooltip;
        })
        .on("mouseout", function () {
            d3.select("#tooltip")
                .classed("hidden", true);
        });
});