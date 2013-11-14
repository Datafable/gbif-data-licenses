// Data

var standard_licenses_datasets = [{"label": "Standard license","color":"#185288","value": 166}, {"label": "Non-standard license","color":"#CCCCCC","value": 11806}];
var standard_licenses_occurrences = [{"label": "Standard license","color":"#185288","value": 9899370}, {"label": "Non-standard license","color":"#CCCCCC","value": 405513274}];

// Add charts to HTML

addPieChart("#chart1","Datasets",standard_licenses_datasets);
addPieChart("#chart2","Occurrences",standard_licenses_occurrences);

// Plot the usage per dataset

nv.addGraph(function() {
var chart = nv.models.multiBarChart()
    .x(function(d) {return d.label})
    .y(function(d) {return d.value})
    //.staggerLabels(true)
    //.tooltips(false)
    //.showValues(true)
    .transitionDuration(100)
    .stacked(true);

d3.select("#chart3")
.datum([{'color': '#03AD0F', 'values': [{'value': 905, 'label': 'usage'}, {'value': 647, 'label': 'distribution'}, {'value': 731, 'label': 'derivatives'}, {'value': 582, 'label': 'commercial'}, {'value': 213, 'label': 'attribution'}, {'value': 178, 'label': 'share alike'}, {'value': 738, 'label': 'notification'}], 'key': 'yes'}, {'color': '#9E9E9E', 'values': [{'value': 10980, 'label': 'usage'}, {'value': 10975, 'label': 'distribution'}, {'value': 10998, 'label': 'derivatives'}, {'value': 11098, 'label': 'commercial'}, {'value': 11139, 'label': 'attribution'}, {'value': 11761, 'label': 'share alike'}, {'value': 11056, 'label': 'notification'}], 'key': 'unknown'}, {'color': '#ED0000', 'values': [{'value': 87, 'label': 'usage'}, {'value': 350, 'label': 'distribution'}, {'value': 243, 'label': 'derivatives'}, {'value': 292, 'label': 'commercial'}, {'value': 620, 'label': 'attribution'}, {'value': 33, 'label': 'share alike'}, {'value': 178, 'label': 'notification'}], 'key': 'no'}]
)
.transition()
.duration(500)
.call(chart);

nv.utils.windowResize(chart.update);

return chart;

} );

// Plot the usage per occurrence

nv.addGraph(function() {
var chart = nv.models.multiBarChart()
    .x(function(d) {return d.label})
    .y(function(d) {return d.value})
    //.staggerLabels(true)
    //.tooltips(false)
    //.showValues(true)
    .transitionDuration(100)
    .stacked(true);

d3.select("#chart4")
.datum([{'color': '#03AD0F', 'values': [{'value': 69775276, 'label': 'usage'}, {'value': 54581128, 'label': 'distribution'}, {'value': 62048951, 'label': 'derivatives'}, {'value': 46952477, 'label': 'commercial'}, {'value': 15075888, 'label': 'attribution'}, {'value': 19026470, 'label': 'share alike'}, {'value': 60420353, 'label': 'notification'}], 'key': 'yes'}, {'color': '#9E9E9E', 'values': [{'value': 343204732, 'label': 'usage'}, {'value': 343830898, 'label': 'distribution'}, {'value': 339051254, 'label': 'derivatives'}, {'value': 339168747, 'label': 'commercial'}, {'value': 333938837, 'label': 'attribution'}, {'value': 395366713, 'label': 'share alike'}, {'value': 332509768, 'label': 'notification'}], 'key': 'unknown'}, {'color': '#ED0000', 'values': [{'value': 2432636, 'label': 'usage'}, {'value': 17000618, 'label': 'distribution'}, {'value': 14312439, 'label': 'derivatives'}, {'value': 29291420, 'label': 'commercial'}, {'value': 66397919, 'label': 'attribution'}, {'value': 1019461, 'label': 'share alike'}, {'value': 22482523, 'label': 'notification'}], 'key': 'no'}])
.transition()
.duration(500)
.call(chart);

nv.utils.windowResize(chart.update);

return chart;

} );

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
