/**
 * Modified from source: https://gist.github.com/jfreels/6814721
 * Purpose: To load a data table and display the converted CSV - JSON Data.
 **/

// This function will be responsible for the creation of the table,
// and will display the csv data but in its converted format of JSON
var createTableData = function (data, columns) {

    // Create some variables for use to store and create our data table
    var table = d3.selectAll('#table-data')
        .append('table')
        .classed('table', 'table table-responsive'); // we add this class to make the table responsive.
    var thead = table.append('thead');
    var tbody = table.append('tbody');

    // Append the Table Head element
    thead.append('tr')
        .selectAll('th')
        .data(columns)
        .enter()
        .append('th')
        .text(function (d) {
            return d
        });

    // Set the properties for each row of data
    var rows = tbody.selectAll('tr')
        .data(data)
        .enter()
        .append('tr');

    // Set the properties for each table cell
    rows.selectAll('td')
        .data(function (row) {
            return columns.map(function (column) {
                return {column: column, value: row[column]}
            });
        })
        .enter()
        .append('td')
        .text(function (d) {
            return d.value
        });

    // return the data-table
    return table;
};

// We call the function to create the table here as well as set which elements of the JSOn file we wish to insert into the table
d3.json('avengers/avengers_project', function (data) {
    var columns = ['Name', 'Current', 'Appearances', 'Gender', 'Year'];
    createTableData(data, columns);
});