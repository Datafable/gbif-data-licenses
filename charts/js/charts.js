// Add charts to HTML

d3.json("data/standard-license-datasets.json", function (data) {
    addPieChart("#chart1","Datasets",data);
});
d3.json("data/standard-license-occurrences.json", function (data) {
    addPieChart("#chart2","Occurrences",data);
});
d3.json("data/parameters-per-dataset.json", function (data) {
    addMultiHorizontalBarChart("#chart3","Datasets",data);
});
d3.json("data/parameters-per-occurrence.json", function(data) {
    addMultiHorizontalBarChart("#chart4","Occurrences",data);
});
d3.json("data/parameters-per-dataset-gbif-dua.json", function(data) {
    addMultiHorizontalBarChart("#chart5","Datasets",data);
});
d3.json("data/parameters-per-occurrence-gbif-dua.json", function(data) {
    addMultiHorizontalBarChart("#chart6","Occurrences",data);
});

// Functions

function addPieChart(element,title,data) {
    // Use this patch for colors to work: https://github.com/novus/nvd3/commit/7dcb8d899bbe6279a71c25e9ea309344924029b9
    nv.addGraph(function() {
        var chart = nv.models.pieChart()
        .x(function(d) {return d.label })
        .y(function(d) {return d.value })
        .valueFormat(d3.format(",d"))
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
        .transitionDuration(100)
        .margin({left: 100, right: 45})
        .stacked(true);

        chart.yAxis.tickFormat(d3.format(",d")); // valueFormat() is available, but has no effect

        d3.select(element)
        .datum(data)
        .transition()
        .duration(500)
        .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
}
