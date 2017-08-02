/**
 * Created by GunnerJnr on 02/04/2017.
 **/

queue()
    .defer(d3.json, "/avengers/avengers_project")
    .await(makeGraphs);

function makeGraphs(error, avengersJson)
{
   // clean projectsJson data
    var avengersProjects = avengersJson;

    // set the format of the date we wish to use
    var dateFormat = d3.time.format("%Y");

    // loop through our data and
    avengersProjects.forEach(function(d)
    {
        // Convert the Year data to a string to be parsed
        d["Year"]  = d["Year"].toFixed();
        // It needs to be a date so it can use a time scale in the bar chart.
        d["Year"] = dateFormat.parse(d["Year"]);
        d["Appearances"] = +d["Appearances"]
    });


   // create a Crossfilter instance for our project
   var ndx = crossfilter(avengersProjects);

   // define all the dimensions we intend to use to display the data
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

   // calculate metrics
   var nameOfCharacter = nameDim.group();
   var current = currentDim.group();
   var gender = genderDim.group();
   var year = yearDim.group();
   var honorary = honoraryDim.group();
   var webLinks = webLinkDim.group();
   // here we group all the relevant data together then reduce the data to return the appearance data we want
   var numOfAppearances = nameDim.group().reduceSum(function (d)
   {
       return d["Appearances"];
   });
   var yearGroup = yearDim.group();
   var nameGroup = nameDim.group();
   var webLinkGroup = webLinkDim.group();

   var all = ndx.groupAll();

   var totalYears = ndx.groupAll().reduceSum(function (d) {
       return d["Year"];
   });

   var max_state = numOfAppearances.top(1)[0].value;

   // define values (to be used in charts)
   var minDate = yearDim.bottom(1)[0]["Year"];
   var maxDate = yearDim.top(1)[0]["Year"];

   var minCurrent = currentDim.bottom(1)[0]["Current"];
   var maxCurrent = currentDim.top(1)[0]["Current"];

   // create the different type of charts for the data to be displayed
   var currentChart = dc.barChart("#current-bar-chart");
   var genderChart = dc.rowChart("#gender-chart");
   var yearChart = dc.barChart("#year-chart");
   var yearND = dc.numberDisplay("#years-nd");
   var honoraryChart = dc.pieChart("#honorary-chart");
   var appearancesND = dc.numberDisplay("#appearances-nd");

   // here we create some drop down select fields to filter the data
   selectField = dc.selectMenu('#year-menu-select')
       .height(300)
       .dimension(yearDim)
       .group(yearGroup);

   selectField = dc.selectMenu('#name-menu-select')
       .height(300)
       .dimension(nameOfCharacter)
       .group(nameDim)
       .group(nameGroup)
       .group(numOfAppearances);

   selectField = dc.selectMenu('#url-menu-select')
       .height(300)
       .dimension(webLinks)
       .group(webLinkDim)
       .group(webLinkGroup);

   genderChart
       .width(600)
       .height(300)
       .dimension(genderDim)
       .group(gender)
       .xAxis().ticks(20);

   // Pie Chart Honorary
    honoraryChart
        .height(300)
        .width(600)
        .radius(125)
        .innerRadius(1)
        .dimension(honoraryDim)
        .group(honorary)
        .colors(d3.scale.ordinal().range(['#20B2AA', '#098bdc', '#ceebfd', '#B0C4DE']))
        .legend(dc.legend().x(25).y(25))
        .minAngleForLabel(0.5) //Only show label in big slices to avoid overlay
        .renderLabel(true)
        .transitionDuration(800);

   yearND
       .height(300)
       .formatNumber(d3.format("d"))
       .valueAccessor(function (d)
       {
           return d;
       })
       .group(all);

   appearancesND
       .height(300)
       .formatNumber(d3.format("d"))
       .valueAccessor(function (d)
       {
           return d;
       })
       .group(all);

   yearChart
       .width(800)
       .height(200)
       .margins({top: 25, right: 10, bottom: 50, left: 30})
       .dimension(yearDim)
       .group(yearGroup)
       .transitionDuration(750)
       .x(d3.time.scale().domain([minDate, maxDate]))
       .elasticY(true)
       .xAxisLabel("Years")
       .yAxis().ticks(10);

   currentChart
       .width(800)
       .height(200)
       .margins({top: 25, right: 10, bottom: 50, left: 30})
       .dimension(yearDim)
       .group(yearGroup)
       .transitionDuration(350)
       .x(d3.time.scale().domain([minDate, maxDate]))
       .y(d3.time.scale().domain([minCurrent, maxCurrent]))
       .elasticY(true)
       .xAxisLabel("Current")
       .yAxis().ticks(10);

   dc.renderAll();

   // hide the loading screen and display the data dashboard
    $('#loading').hide();
    $('#loading-screen').hide();
}