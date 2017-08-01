/// Create our crossfilter instance

//// We need to first clear all filters and then it will work. It’s good practice to always clear filters before starting another one. (typeDim.filterAll())

// ----------------------------------------NUMBERS----------------------------------------//

// create a variable to store the cross filter data array
var ndx = crossfilter(data);

// get all the transactions with a total equal to 90
var totalDim = ndx.dimension(function (d) {
    return d.total;
});

// start to filter our data, find all the totals equal to 90
var total_90 = totalDim.filterExact(90);

// to filter between 90 and 100 [we need to got to 101 to include 100]
var total_90_101 = totalDim.filter([90, 101]);

// to filter items divisible by three 
var total_3 = totalDim.filter(function (d) {
    if (d % 3 === 0) {
        return d;
    }
});

// ----------------------------------------STRINGS----------------------------------------//

// filter & find the types where the customers used visa
var typeDim = ndx.dimension(function (d) {
    return d.type;
});
var visa_filter = typeDim.filter("visa");
var cash_filter = typeDim.filter("cash");

// sum up the cash totals using the reduceSum function
var total = typeDim.group().reduceSum(function (d) {
    return d.total;
});

// to get the total cash you use groupall on the crossfilter object itself, this observes
// all filters, so when we do a reduceSum we get the sum of the total column for the current
// filter
var cash_total = ndx.groupAll().reduceSum(function (d) {
    return d.total;
}).value();
console.log("cash_total = " + cash_total);

typeDim.filterAll()

var cash_and_visa_filter = typeDim.filter(function (d) {
    if (d === "visa" || d === "cash") {
        return d;
    }
});

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

// ----------------------------------------OUTPUTS----------------------------------------//

// print the filtered results to the browser console (f12 dev tools to view)
print_filter("total_90");
print_filter("total_90_101");
print_filter("total_3");

print_filter("visa_filter");
print_filter("cash_filter");
print_filter("total");
print_filter("cash_and_visa_filter");