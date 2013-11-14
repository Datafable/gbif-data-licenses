// Data

var standard_licenses_datasets = [{"label": "Standard license","color":"#185288","value": 166}, {"label": "Non-standard license","color":"#CCCCCC","value": 11806}];
var standard_licenses_occurrences = [{"label": "Standard license","color":"#185288","value": 9899370}, {"label": "Non-standard license","color":"#CCCCCC","value": 405513274}];

// Add charts to HTML

addPieChart("#chart1","Datasets",standard_licenses_datasets);
addPieChart("#chart2","Occurrences",standard_licenses_occurrences);

// Functions

function addPieChart(element,title,data) {
    // Use this patch for colors to work: https://github.com/novus/nvd3/commit/7dcb8d899bbe6279a71c25e9ea309344924029b9
    nv.addGraph(function() {
        var chart = nv.models.pieChart()
        .x(function(d) {return d.label })
        .y(function(d) {return d.value })
        .valueFormat(d3.format(',.0f'))
        .showLabels(false)
        .donut(true);

        d3.select(element)
        .datum(data)
        .transition()
        .duration(1200)
        .call(chart);

        d3.select(element)
        .append("text")
        .attr("x","50%")
        .attr("y","52%")
        .attr("text-anchor","middle")
        .attr("class","title")
        .text(title);

        return chart;
    });
}
