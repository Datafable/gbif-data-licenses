// Data

var standard_licenses_datasets = [{"label": "Standard license","color":"#27AE60","value": 166}, {"label": "Non-standard license","color":"#CCCCCC","value": 11806}];
var standard_licenses_occurrences = [{"label": "Standard license","color":"#27AE60","value": 9899370}, {"label": "Non-standard license","color":"#CCCCCC","value": 405513274}];
var general_use_parameters_datasets = [{"key": "Open", "color": "#27AE60", "values": [{"value": 905, "label": "Use"}, {"value": 647, "label": "Distribution"}, {"value": 731, "label": "Derivatives"}, {"value": 582, "label": "Commercial use"}, {"value": 213, "label": "Attribution"}, {"value": 178, "label": "Share alike"}, {"value": 738, "label": "Notification"}]}, {"key": "Unclear", "color": "#CCCCCC", "values": [{"value": 10980, "label": "Use"}, {"value": 10975, "label": "Distribution"}, {"value": 10998, "label": "Derivatives"}, {"value": 11098, "label": "Commercial use"}, {"value": 11139, "label": "Attribution"}, {"value": 11761, "label": "Share alike"}, {"value": 11056, "label": "Notification"}]}, {"key": "Restricted/Required", "color": "#C0392B", "values": [{"value": 87, "label": "Use"}, {"value": 350, "label": "Distribution"}, {"value": 243, "label": "Derivatives"}, {"value": 292, "label": "Commercial use"}, {"value": 620, "label": "Attribution"}, {"value": 33, "label": "Share alike"}, {"value": 178, "label": "Notification"}]}];
var general_use_parameters_occurrences = [{"key": "Open", "color": "#27AE60", "values": [{"value": 69775276, "label": "Use"}, {"value": 54581128, "label": "Distribution"}, {"value": 62048951, "label": "Derivatives"}, {"value": 46952477, "label": "Commercial use"}, {"value": 15075888, "label": "Attribution"}, {"value": 19026470, "label": "Share alike"}, {"value": 60420353, "label": "Notification"}]}, {"key": "Unclear", "color": "#CCCCCC", "values": [{"value": 343204732, "label": "Use"}, {"value": 343830898, "label": "Distribution"}, {"value": 339051254, "label": "Derivatives"}, {"value": 339168747, "label": "Commercial use"}, {"value": 333938837, "label": "Attribution"}, {"value": 395366713, "label": "Share alike"}, {"value": 332509768, "label": "Notification"}]}, {"key": "Restriced/Required", "color": "#C0392B", "values": [{"value": 2432636, "label": "Use"}, {"value": 17000618, "label": "Distribution"}, {"value": 14312439, "label": "Derivatives"}, {"value": 29291420, "label": "Commercial use"}, {"value": 66397919, "label": "Attribution"}, {"value": 1019461, "label": "Share alike"}, {"value": 22482523, "label": "Notification"}]}];

// Add charts to HTML

addPieChart("#chart1","Datasets",standard_licenses_datasets);
addPieChart("#chart2","Occurrences",standard_licenses_occurrences);
addMultiHorizontalBarChart("#chart3","Datasets",general_use_parameters_datasets);
addMultiHorizontalBarChart("#chart4","Occurrences",general_use_parameters_occurrences);

// Functions

function addPieChart(element,title,data) {
    // Use this patch for colors to work: https://github.com/novus/nvd3/commit/7dcb8d899bbe6279a71c25e9ea309344924029b9
    nv.addGraph(function() {
        var chart = nv.models.pieChart()
        .x(function(d) {return d.label })
        .y(function(d) {return d.value })
        .valueFormat(d3.format("f"))
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

        nv.utils.windowResize(chart.update);

        return chart;
    });
}

function addMultiHorizontalBarChart(element,title,data) {
    nv.addGraph(function() {
        var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) {return d.label})
        .y(function(d) {return d.value})
        .valueFormat(d3.format('f')) // Doesn't seem to have an effect
        .transitionDuration(100)
        .margin({left: 100})
        .stacked(true);

        d3.select(element)
        .datum(data)
        .transition()
        .duration(500)
        .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
}
