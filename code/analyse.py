#!/usr/bin/python

#================================================
# This file contains several methods that can be
# used to analyse the data. It prints some output
# That can be used for creating visualizations.
#================================================

import pandas as pd
from IPython import embed

def get_data(infile):
    df = pd.read_csv(open(infile), sep=',', header=0)
    return df

def get_total_nr_of_occurrences(data):
    total_sum = data['numberOfOccurrences'].apply(int).sum()
    print 'total number of occurrences: {0}'.format(total_sum)
    return total_sum

def get_total_nr_of_datasets(data):
    total = len(data)
    return total

def get_nr_of_datasets_with_standard_license(data):
    subset = data[data['standard license'].notnull()]
    return len(subset)

def get_number_of_datasets_where_use_true(data):
    subset = data[data['use'] == 'true']
    return len(subset)

def get_number_of_datasets_where_use_false(data):
    subset = data[data['use'] == 'false']
    return len(subset)

def get_number_of_datasets_where_use_unknown(data):
    subset = data[data['use'] == '?']
    return len(subset)

def nr_of_occurrences_with_standard_license(data):
    subset = data[data['standard license'].notnull()]
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    print 'number of occurrences with standard licenses: {0}'.format(subset_sum)
    return subset_sum

def get_html_header():
    return """
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script src="../lib/d3.v3.min.js"></script>
    <script src="../lib/novus-nvd3-764767a/nv.d3.min.js"></script>
    <link href="../lib/novus-nvd3-764767a/src/nv.d3.css" rel="stylesheet" type="text/css">
    <script src="../lib/novus-nvd3-764767a/src/utils.js"></script>
    <script src="../lib/novus-nvd3-764767a/src/models/pie.js"></script>
    """

def generate_bar_chart_html(chart_title, categories, chart_data, plotnr):
    index_html = '<div id="container{0}" style="width:100%; height: 400px;"></div>'.format(plotnr)
    chart_js_code = '<script>$(function() {{$("#container{0}").highcharts({{chart: {{type: "bar", plotBorderWidth: 6}}, title: {{text: "{1}" }}, xAxis: {{categories: {2}}}, yAxis: {{title: {{text: "Number of occurrences"}} }}, series: {3} }});}});</script>'.format(plotnr, chart_title, categories, chart_data)
    return index_html + chart_js_code

def generate_pie_chart_html(chart_title, chart_data, plotnr):
    index_html =  '<svg id="container{0}" style="width:60%; height: 400px;"></svg>\n'.format(plotnr)
    chart_js_code = """<script>
    nv.addGraph(function() {{
	var chart = nv.models.pieChart()
	.x(function(d) {{return d.label }})
	.y(function(d) {{return d.value }})
	.showLabels(true);

	d3.select("#container{1}")
	.datum(exampleData())
	.transition()
	.duration(1200)
	.call(chart);

	return chart;
    }} );

    function exampleData() {{
	return {0};
    }}
    </script>
    """.format(chart_data, plotnr)
    return index_html + chart_js_code

def main():
    data = get_data('data/joined_data.csv')
    total_oc = get_total_nr_of_occurrences(data)
    nr_oc_std_lic = nr_of_occurrences_with_standard_license(data)
    nr_oc_no_std_lic = total_oc - nr_oc_std_lic
    license_data = {'key': 'occurrences', 'values': [{'label': 'standard license', 'value': nr_oc_std_lic}, {'label': 'no standard license', 'value': nr_oc_no_std_lic}]}
    print license_data

    total_nr_ds = get_total_nr_of_datasets(data)
    nr_ds_std_lic = get_nr_of_datasets_with_standard_license(data)
    nr_ds_no_std_lic = total_nr_ds - nr_ds_std_lic
    license_data = {'key': 'datasets', 'values': [{'label': 'standard license', 'value': nr_ds_std_lic}, {'label': 'no standard license', 'value': nr_ds_no_std_lic}]}
    print license_data

    nr_ds_use_true = get_number_of_datasets_where_use_true(data)
    nr_ds_use_false = get_number_of_datasets_where_use_false(data)
    nr_ds_use_unknown = get_number_of_datasets_where_use_unknown(data)
    use_data = {'key': 'datasets', 'values': [{'label': 'yes', 'value': nr_ds_use_true}, {'label': 'no', 'value': nr_ds_use_false}, {'label': 'unknown', 'value': nr_ds_use_unknown}]}
    print 'usage per dataset'
    print use_data

main()
