/**
 * Modified from source: https://gist.github.com/jfreels/6814721
 **/

var createTableData = function(data, columns)
{
  var table = d3.selectAll('#url-table-data').append('table');
  var thead = table.append('thead');
  var tbody = table.append('tbody');

  thead.append('tr')
      .selectAll('th')
      .data(columns)
      .enter()
      .append('th')
      .text(function (d)
      {
          return d
      });

  var rows = tbody.selectAll('tr')
      .data(data)
      .enter()
      .append('tr');

  var cells = rows.selectAll('td')
      .data(function(row)
      {
          return columns.map(function (column)
          {
              return { column: column, value: row[column] }
	      });
      })
      .enter()
      .append('td')
      .text(function (d)
      {
          return d.value
      });

  return table;
};

d3.csv('avengers/avengers_project',function (data)
{
    var columns = ['URL', 'Notes', 'Gender', 'Year', 'Death1', 'Return1'];
    createTableData(data, columns);
});