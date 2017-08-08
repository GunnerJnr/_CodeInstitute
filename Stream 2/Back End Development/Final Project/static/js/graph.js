/**
 * Created by GunnerJnr on 02/04/2017.
 **/

queue()
    .defer(d3.json, "/avengers/avengers_project")
    .await(makeGraphs);

function makeGraphs(error, avengersJson) {

    // throw an error message if we cannot fetch the data
    if (error) {
        console.error("makeGraphs error on receiving data set:", error.statusText);
        throw error;
    }

    // Clean projectsJson data
    var avengersProjects = avengersJson;

    // Set the format of the date we wish to use
    var dateFormat = d3.time.format("%Y");

    // Loop through our data and
    avengersProjects.forEach(function (d) {
        // Convert the Year data to a string to be parsed
        d["Year"] = d["Year"].toFixed();
        // It needs to be a date so it can use a time scale in the bar chart.
        d["Year"] = dateFormat.parse(d["Year"]);
        d["Appearances"] = +d["Appearances"]
    });


    // Create a Crossfilter instance for our project
    var ndx = crossfilter(avengersProjects);

    // Define all the dimensions we intend to use to display the data
    var nameDim = ndx.dimension(function (d) {
        return d["Name"];
    });
    var currentDim = ndx.dimension(function (d) {
        return d["Current"];
    });
    var genderDim = ndx.dimension(function (d) {
        return d["Gender"];
    });
    var yearDim = ndx.dimension(function (d) {
        return d["Year"];
    });
    var honoraryDim = ndx.dimension(function (d) {
        return d["Honorary"];
    });
    var webLinkDim = ndx.dimension(function (d) {
        return d["URL"];
    });

    // Calculate metrics
    var current = currentDim.group();
    var gender = genderDim.group();
    var year = yearDim.group();
    var honorary = honoraryDim.group();

    // Here we group all the relevant data together then reduce the data to return the appearance data we want
    var yearGroup = yearDim.group();
    var nameGroup = nameDim.group();
    var webLinkGroup = webLinkDim.group();
    var all = ndx.groupAll();

    // define values (to be used in charts)
    var minDate = yearDim.bottom(1)[0]["Year"];
    var maxDate = yearDim.top(1)[0]["Year"];

    var minCurrent = currentDim.bottom(1)[0]["Current"];
    var maxCurrent = currentDim.top(1)[0]["Current"];

    // create the different type of charts for the data to be displayed
    var currentChart = dc.barChart("#current-bar-chart");
    var genderChart = dc.rowChart("#gender-row-chart");
    var yearChart = dc.barChart("#year-bar-chart");
    var yearND = dc.numberDisplay("#years-nd");
    var honoraryChart = dc.pieChart("#honorary-pie-chart");
    var appearancesND = dc.numberDisplay("#appearances-nd");

    // here we create some drop down select fields to filter the data
    dc.selectMenu('#year-menu-select')
        .width(600)
        .height(300)
        .dimension(yearDim)
        .group(yearGroup);
    dc.selectMenu('#name-menu-select')
        .width(600)
        .height(300)
        .dimension(nameDim)
        .group(nameGroup);
    dc.selectMenu('#url-menu-select')
        .width(600)
        .height(300)
        .dimension(webLinkDim)
        .group(webLinkGroup);

    // Row Chart Gender
    genderChart
        .width(600)
        .height(300)
        .dimension(genderDim)
        .group(gender)
        .xAxis().ticks(10);

    // Pie Chart Honorary
    honoraryChart
        .height(300)
        .width(600)
        .radius(125)
        .innerRadius(1)
        .dimension(honoraryDim)
        .group(honorary)
        .colors(d3.scale.ordinal().range(['#20B2AA', '#098bdc', '#ceebfd', '#B0C4DE']))
        .legend(dc.legend().x(30).y(30))
        .minAngleForLabel(45) //Only show label in big slices to avoid overlay
        .renderLabel(true)
        .transitionDuration(500);

    // Total Num of Years displayed
    yearND
        .height(300)
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) {
            return d;
        })
        .group(all);

    // Total num of Appearances displayed
    appearancesND
        .height(300)
        .formatNumber(d3.format("d"))
        .valueAccessor(function (d) {
            return d;
        })
        .group(all);

    // Year bar chart
    yearChart
        .width(600)
        .height(200)
        .margins({top: 25, right: 5, bottom: 50, left: 5})
        .dimension(yearDim)
        .group(yearGroup)
        .transitionDuration(650)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .elasticY(true)
        .xAxisLabel("Years")
        .yAxis().ticks(8);

    // Is the avenger still current - bar chart
    currentChart
        .width(600)
        .height(200)
        .margins({top: 25, right: 5, bottom: 50, left: 5})
        .dimension(yearDim)
        .group(yearGroup)
        .transitionDuration(650)
        .x(d3.time.scale().domain([minDate, maxDate]))
        .y(d3.time.scale().domain([minCurrent, maxCurrent]))
        .elasticY(true)
        .xAxisLabel("Current")
        .yAxis().ticks(8);

    // Finally we want to render all the charts and date to the dashboard
    dc.renderAll();

    // Hide the loading screen and display the data dashboard
    $('#loading').hide();
    $('#loading-screen').hide();
}