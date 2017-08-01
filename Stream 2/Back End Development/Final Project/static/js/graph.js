/**
 * Created by GunnerJnr on 02/04/2017.
 */
queue()
    .defer(d3.json, "/avengers/avengers_project")
   .await(makeGraphs);

function makeGraphs(error, avengersJson) {

   //Clean projectsJson data
    var avengersProjects = avengersJson;

   var dateFormat = d3.time.format("%Y");
   avengersProjects.forEach(function(d){
        d["Year"]  = d["Year"].toFixed(); // Convert Year to string to be parsed
        d["Year"] = dateFormat.parse(d["Year"]); // It needs to be a date to use a time scale in the bar chart.
        d["Appearances"] = +d["Appearances"]
    });


   //Create a Crossfilter instance
   var ndx = crossfilter(avengersProjects);

   //Define Dimensions
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


   //Calculate metrics
   var nameOfCharacter = nameDim.group();
   var current = currentDim.group();
   var gender = genderDim.group();
   var year = yearDim.group();
   var honorary = honoraryDim.group();
   var webLinks = webLinkDim.group();
   var numOfAppearances = nameDim.group().reduceSum(function (d) {
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

   //Define values (to be used in charts)
   var minDate = yearDim.bottom(1)[0]["Year"];
   var maxDate = yearDim.top(1)[0]["Year"];

   //Charts
   var currentChart = dc.rowChart("#current-chart");
   var genderChart = dc.rowChart("#gender-chart");
   var yearChart = dc.barChart("#year-chart")
   var yearND = dc.numberDisplay("#years-nd");
   var honoraryChart = dc.pieChart("#honorary-chart");
   var appearancesND = dc.numberDisplay("#appearances-nd")

    var selectField = dc.selectMenu('#year-menu-select')
        .dimension(yearDim)
        .group(yearGroup)

   var selectField = dc.selectMenu('#name-menu-select')
       .dimension(nameOfCharacter)
       .group(nameDim)
       .group(nameGroup)
       .group(numOfAppearances);

   var selectField = dc.selectMenu('#url-menu-select')
       .dimension(webLinks)
       .group(webLinkDim)
       .group(webLinkGroup);

   yearChart
        .width(800)
       .height(200)
       .margins({top: 25, right: 50, bottom: 30, left: 50})
       .dimension(yearDim)
       .group(yearGroup)
       .transitionDuration(500)
       .x(d3.time.scale().domain([minDate, maxDate]))
       .elasticY(true)
       .xAxisLabel("Years")
       .yAxis().ticks(6);

   yearND
       .formatNumber(d3.format("d"))
       .valueAccessor(function (d) {
           return d;
       })
       .group(all);

   // Pie Chart Honorary
    honoraryChart
        .height(220)
        .radius(90)
        .width(300)
        .innerRadius(40)
        .dimension(honoraryDim)
        .group(honorary)
        .colors(d3.scale.ordinal().range(['#20B2AA', '#098bdc', '#ceebfd', '#B0C4DE']))
        .legend(dc.legend().x(0).y(10))
        .minAngleForLabel(0.5) //Only show label in big slices to avoid overlay
        .externalLabels(0.05) //Separate the labels from the center of the pie
        .renderLabel(true)
        .transitionDuration(500);

   currentChart
       .width(300)
       .height(250)
       .dimension(currentDim)
       .group(current)
       .xAxis().ticks(4);

   genderChart
       .width(300)
       .height(250)
       .dimension(genderDim)
       .group(gender)
       .xAxis().ticks(4);

   appearancesND
       .formatNumber(d3.format("d"))
       .valueAccessor(function (d) {
           return d;
       })
       .group(all);

   dc.renderAll();
}