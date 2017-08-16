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
            date: "12/28/2011",
            http_404: 2,
            http_200: 10,
            http_302: 100
    },
        {
            date: "12/29/2016",
            http_404: 1,
            http_200: 300,
            http_302: 200
    },
        {
            date: "12/30/2013",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "12/31/2013",
            http_404: 2,
            http_200: 290,
            http_302: 20
    },
        {
            date: "01/01/2014",
            http_404: 2,
            http_200: 910,
            http_302: 6
    },
        {
            date: "01/02/2014",
            http_404: 11,
            http_200: 10,
            http_302: 21
    },
        {
            date: "01/03/2014",
            http_404: 2,
            http_200: 90,
            http_302: 0
    },
        {
            date: "01/04/2015",
            http_404: 223,
            http_200: 490,
            http_302: 200
    },
        {
            date: "01/05/2015",
            http_404: 12,
            http_200: 910,
            http_302: 20
    },
        {
            date: "01/06/2015",
            http_404: 32,
            http_200: 200,
            http_302: 15
    },
        {
            date: "01/07/2016",
            http_404: 19,
            http_200: 200,
            http_302: 100
    },

        {
            date: "21/06/2016",
            http_404: 21,
            http_200: 910,
            http_302: 50
    },
        {
            date: "11/08/2011",
            http_404: 25,
            http_200: 890,
            http_302: 10
    },
        {
            date: "29/03/2011",
            http_404: 267,
            http_200: 2100,
            http_302: 143
    },
        {
            date: "01/07/2012",
            http_404: 11,
            http_200: 2010,
            http_302: 1100
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
    /*var hits = dateDim.group().reduceSum(function (d) {
        return d.total;
    });*/

    // create a  group  for http_status_200 and stack groups for status_302 and status_404 messages on top so we get a filled-in line chart for each grouping
    var status_200 = dateDim.group().reduceSum(function (d) {
        return d.http_200;
    });
    var status_302 = dateDim.group().reduceSum(function (d) {
        return d.http_302;
    });
    var status_404 = dateDim.group().reduceSum(function (d) {
        return d.http_404;
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
        .width(500).height(200)
        .dimension(dateDim)
        .group(status_200, "200") // group the status 200
        .stack(status_302, "302") // stack these on top
        .stack(status_404, "404") // ...
        .renderArea(true) // add colour to fill the lines
        .brushOn(false) // turn the chart brush off (on by default)
        .colors(["#FFFF66", "#FF3300", "#3399FF", "#00E6E6", "#FF5500"]) // style it with color
        .x(d3.time.scale().domain([minDate, maxDate]))
        .legend(dc.legend().x(450).y(10).itemHeight(13).gap(5)) // add an interactive legend
        .yAxisLabel("Hits per day"); // label the y axis

    // set the pie chart properties -
    hitspieChart
        .width(190)
        .height(190)
        .slicesCap(10)
        .innerRadius(50)
        .dimension(yearDim)
        .group(year_total);

    // add a table to marry up with the charts as a visual aid
    var datatable = dc.dataTable("#dc-data-table");

    // create the table and set the properties
    datatable
        .dimension(dateDim)
        .group(function (d) {
            return d.Year;
        })
        // create the columns dynamically
        .columns([
       function (d) {
                return d.date.getDate() + "/" + (d.date.getMonth() + 1) + "/" + d.date.getFullYear();
       },
       function (d) {
                return d.http_200;
       },
       function (d) {
                return d.http_302;
       },
       function (d) {
                return d.http_404;
       },
       function (d) {
                return d.total;
       }
   ]);

    // tell dc to render the chart:
    dc.renderAll();
};