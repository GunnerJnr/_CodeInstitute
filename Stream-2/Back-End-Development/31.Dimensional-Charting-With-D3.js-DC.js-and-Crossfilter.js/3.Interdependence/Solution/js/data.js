// ensure we wait until the page has fully loaded before loading the scripts 
// (only really necessary in the head tags in the HTML doc)
window.onload = function () {

    // ----------------------------------------HELPERS----------------------------------------//

    // Helper function so we are able to test our filter works
    function print_filter(filter) {
        var f = eval(filter);
        if (typeof (f.length) != "undefined") {} else {}
        if (typeof (f.top) != "undefined") {
            f = f.top(Infinity);
        } else {}
        if (typeof (f.dimension) != "undefined") {
            f = f.dimension(function (d) {
                return "";
            }).top(Infinity);
        } else {}
        console.log(filter + "(" + f.length + ") = " + JSON.stringify(f).replace("[", "[\n\t").replace(/}\,/g, "},\n\t").replace("]", "\n]"));
    }

    // The inspiration for this graph is everyday our servers get hit. 
    // We want to draw a simple line graph showing how many hits we get per day, 
    // some are valid (200s), some are redirects (302s), and some are broken links (404s). 
    // The way the data is laid out is very concise.

    // create an array to store our data
    var data = [
        {
            date: "12/27/2012",
            http_404: 2,
            http_200: 190,
            http_302: 100
    },
        {
            date: "12/28/2012",
            http_404: 2,
            http_200: 10,
            http_302: 100
    },
        {
            date: "12/29/2012",
            http_404: 1,
            http_200: 300,
            http_302: 200
    },
        {
            date: "12/30/2012",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "12/31/2012",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/01/2013",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/02/2013",
            http_404: 1,
            http_200: 10,
            http_302: 1
    },
        {
            date: "01/03/2013",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/04/2013",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/05/2013",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/06/2013",
            http_404: 2,
            http_200: 200,
            http_302: 1
    },
        {
            date: "01/07/2013",
            http_404: 1,
            http_200: 200,
            http_302: 100
    }
		];

    // store the array data and set up the crossfilter
    var ndx = crossfilter(data);

    // let dc.js know its a date by specifying a date format
    var parseDate = d3.time.format("%m/%d/%Y").parse;

    data.forEach(function (d) {
        d.date = parseDate(d.date); // get and parse the date
        d.total = d.http_404 + d.http_200 + d.http_302; // get the hits
        d.Year = d.date.getFullYear(); // get the year
    });

    // print to console (F12 dev tools in chrome to view)
    print_filter("data");

    // we will create a date dimension for the x axis, for the y axis we will show the total number of hits
    var dateDim = ndx.dimension(function (d) {
        return d.date;
    });
    var hits = dateDim.group().reduceSum(function (d) {
        return d.total;
    });

    // create a dim to get the year
    var yearDim = ndx.dimension(function (d) {
        return +d.Year;
    });

    // create and fetch the tyearly total
    var year_total = yearDim.group().reduceSum(function (d) {
        return d.total;
    });

    // DC has a nice function so we can shorten the syntax by using dc.pluck instead of inline function
    //var hits = dateDim.group().reduceSum(dc.pluck('total'));

    // range for x-axis. For this, we want to get the min and max date in our array.
    // We can do this by using the crossfilter functions to get the:
    // bottom value and the top value for the date column
    var minDate = dateDim.bottom(1)[0].date;
    var maxDate = dateDim.top(1)[0].date;

    // associate our chart with the DOM element
    var hitslineChart = dc.lineChart("#chart-line-hitsperday"); // line chart
    var hitspieChart = dc.pieChart("#chart-ring-year"); // pie chart

    // set the line charts properties - dimension (x-axis), group (y-axis), and range
    hitslineChart
        .width(500)
        .height(200)
        .brushOn(false) // turn off the chart brush (on by default)
        .yAxisLabel("Hits per day") // label the Yaxis
        .dimension(dateDim)
        .group(hits)
        .x(d3.time.scale().domain([minDate, maxDate]));

    // set the pie chart properties -
    hitspieChart
        .width(190)
        .height(190)
        .slicesCap(4)
        .innerRadius(50)
        .dimension(yearDim)
        .group(year_total);

    // tell dc to render the chart:
    dc.renderAll();
};