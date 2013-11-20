#!/usr/bin/python

#================================================
# This file contains several methods that can be
# used to analyse the data. It prints some output
# That can be used for creating visualizations.
#================================================

import sys
import pandas as pd
import simplejson as json

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

def nr_of_occurrences_with_standard_license(data):
    subset = data[data['standard license'].notnull()]
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    print 'number of occurrences with standard licenses: {0}'.format(subset_sum)
    return subset_sum

#----------------------------
# The following methods calculate the number of datasets having a license with specific parameters
#----------------------------
def get_number_of_datasets_where_use_true(data):
    subset = data[data['use'] == 'true']
    return len(subset)

def get_number_of_datasets_where_use_false(data):
    subset = data[data['use'] == 'false']
    return len(subset)

def get_number_of_datasets_where_use_unknown(data):
    subset = data[data['use'] == '?']
    return len(subset)

def get_number_of_datasets_where_distrib_true(data):
    subset = data[data['distribution'] == 'true']
    return len(subset)

def get_number_of_datasets_where_distrib_false(data):
    subset = data[data['distribution'] == 'false']
    return len(subset)

def get_number_of_datasets_where_distrib_unknown(data):
    subset = data[data['distribution'] == '?']
    return len(subset)

def get_number_of_datasets_where_deriv_true(data):
    subset = data[data['derivatives'] == 'true']
    return len(subset)

def get_number_of_datasets_where_deriv_false(data):
    subset = data[data['derivatives'] == 'false']
    return len(subset)

def get_number_of_datasets_where_deriv_unknown(data):
    subset = data[data['derivatives'] == '?']
    return len(subset)

def get_number_of_datasets_where_commer_true(data):
    subset = data[data['commercial'] == 'true']
    return len(subset)

def get_number_of_datasets_where_commer_false(data):
    subset = data[data['commercial'] == 'false']
    return len(subset)

def get_number_of_datasets_where_commer_unknown(data):
    subset = data[data['commercial'] == '?']
    return len(subset)

def get_number_of_datasets_where_attrib_true(data):
    subset = data[data['attribution'] == 'true']
    return len(subset)

def get_number_of_datasets_where_attrib_false(data):
    subset = data[data['attribution'] == 'false']
    return len(subset)

def get_number_of_datasets_where_attrib_unknown(data):
    subset = data[data['attribution'] == '?']
    return len(subset)

def get_number_of_datasets_where_share_true(data):
    subset = data[data['share alike'] == 'true']
    return len(subset)

def get_number_of_datasets_where_share_false(data):
    subset = data[data['share alike'] == 'false']
    return len(subset)

def get_number_of_datasets_where_share_unknown(data):
    subset = data[data['share alike'] == '?']
    return len(subset)

def get_number_of_datasets_where_notific_true(data):
    subset = data[data['notification'] == 'true']
    return len(subset)

def get_number_of_datasets_where_notific_false(data):
    subset = data[data['notification'] == 'false']
    return len(subset)

def get_number_of_datasets_where_notific_unknown(data):
    subset = data[data['notification'] == '?']
    return len(subset)

#----------------------------
# The following methods calculate the number of occurrences having a license with specific parameters
#----------------------------
def get_number_of_occ_where_use_true(data):
    subset = data[data['use'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_use_false(data):
    subset = data[data['use'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_use_unknown(data):
    subset = data[data['use'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_distrib_true(data):
    subset = data[data['distribution'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_distrib_false(data):
    subset = data[data['distribution'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_distrib_unknown(data):
    subset = data[data['distribution'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_deriv_true(data):
    subset = data[data['derivatives'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_deriv_false(data):
    subset = data[data['derivatives'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_deriv_unknown(data):
    subset = data[data['derivatives'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_commer_true(data):
    subset = data[data['commercial'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_commer_false(data):
    subset = data[data['commercial'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_commer_unknown(data):
    subset = data[data['commercial'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_attrib_true(data):
    subset = data[data['attribution'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_attrib_false(data):
    subset = data[data['attribution'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_attrib_unknown(data):
    subset = data[data['attribution'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_share_true(data):
    subset = data[data['share alike'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_share_false(data):
    subset = data[data['share alike'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_share_unknown(data):
    subset = data[data['share alike'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_notific_true(data):
    subset = data[data['notification'] == 'true']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_notific_false(data):
    subset = data[data['notification'] == 'false']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

def get_number_of_occ_where_notific_unknown(data):
    subset = data[data['notification'] == '?']
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    return subset_sum

#----------------------------
# Wrapper methods
#----------------------------
def analyse_parameters_per_dataset(data):
    nr_ds_use_ok = get_number_of_datasets_where_use_true(data)
    nr_ds_use_notok= get_number_of_datasets_where_use_false(data)
    nr_ds_use_unknown = get_number_of_datasets_where_use_unknown(data)

    nr_ds_distrib_ok = get_number_of_datasets_where_distrib_true(data)
    nr_ds_distrib_notok = get_number_of_datasets_where_distrib_false(data)
    nr_ds_distrib_unknown = get_number_of_datasets_where_distrib_unknown(data)

    nr_ds_deriv_ok = get_number_of_datasets_where_deriv_true(data)
    nr_ds_deriv_notok = get_number_of_datasets_where_deriv_false(data)
    nr_ds_deriv_unknown = get_number_of_datasets_where_deriv_unknown(data)

    nr_ds_commer_ok = get_number_of_datasets_where_commer_true(data)
    nr_ds_commer_notok = get_number_of_datasets_where_commer_false(data)
    nr_ds_commer_unknown = get_number_of_datasets_where_commer_unknown(data)

    nr_ds_attrib_notok = get_number_of_datasets_where_attrib_true(data)
    nr_ds_attrib_ok = get_number_of_datasets_where_attrib_false(data)
    nr_ds_attrib_unknown = get_number_of_datasets_where_attrib_unknown(data)

    nr_ds_share_notok = get_number_of_datasets_where_share_true(data)
    nr_ds_share_ok = get_number_of_datasets_where_share_false(data)
    nr_ds_share_unknown = get_number_of_datasets_where_share_unknown(data)

    nr_ds_notific_notok = get_number_of_datasets_where_notific_true(data)
    nr_ds_notific_ok = get_number_of_datasets_where_notific_false(data)
    nr_ds_notific_unknown = get_number_of_datasets_where_notific_unknown(data)

    color_ds_ok = '#27AE60'
    color_ds_notok = '#CCCCCC'
    color_ds_unknown = '#C0392B'

    label_ds_ok = 'Open'
    label_ds_notok = 'Restricted/Required'
    label_ds_unknown = 'Unclear'

    label_ds_use = 'Use'
    label_ds_distrib = 'Distribution'
    label_ds_deriv = 'Derivatives'
    label_ds_commer = 'Commercial'
    label_ds_attrib = 'Attribution'
    label_ds_share = 'Share alike'
    label_ds_notific = 'Notification'

    results_json = [
    {'color': color_ds_ok, 'key': label_ds_ok, 'values': [
        {'label': label_ds_use, 'value': int(nr_ds_use_ok)},
        {'label': label_ds_distrib, 'value': int(nr_ds_distrib_ok)},
        {'label': label_ds_deriv, 'value': int(nr_ds_deriv_ok)},
        {'label': label_ds_commer, 'value': int(nr_ds_commer_ok)},
        {'label': label_ds_attrib, 'value': int(nr_ds_attrib_ok)},
        {'label': label_ds_share, 'value': int(nr_ds_share_ok)},
        {'label': label_ds_notific, 'value': int(nr_ds_notific_ok)}
    ]},
    {'color': color_ds_unknown, 'key': label_ds_unknown, 'values': [
        {'label': label_ds_use, 'value': int(nr_ds_use_unknown)},
        {'label': label_ds_distrib, 'value': int(nr_ds_distrib_unknown)},
        {'label': label_ds_deriv, 'value': int(nr_ds_deriv_unknown)},
        {'label': label_ds_commer, 'value': int(nr_ds_commer_unknown)},
        {'label': label_ds_attrib, 'value': int(nr_ds_attrib_unknown)},
        {'label': label_ds_share, 'value': int(nr_ds_share_unknown)},
        {'label': label_ds_notific, 'value': int(nr_ds_notific_unknown)}
    ]},
    {'color': color_ds_notok, 'key': label_ds_notok, 'values': [
        {'label': label_ds_use, 'value': int(nr_ds_use_notok)},
        {'label': label_ds_distrib, 'value': int(nr_ds_distrib_notok)},
        {'label': label_ds_deriv, 'value': int(nr_ds_deriv_notok)},
        {'label': label_ds_commer, 'value': int(nr_ds_commer_notok)},
        {'label': label_ds_attrib, 'value': int(nr_ds_attrib_notok)},
        {'label': label_ds_share, 'value': int(nr_ds_share_notok)},
        {'label': label_ds_notific, 'value': int(nr_ds_notific_notok)}
    ]}
    ]
    return results_json

def analyse_parameters_per_occurrence(data):
    nr_occ_use_ok = get_number_of_occ_where_use_true(data)
    nr_occ_use_notok= get_number_of_occ_where_use_false(data)
    nr_occ_use_unknown = get_number_of_occ_where_use_unknown(data)

    nr_occ_distrib_ok = get_number_of_occ_where_distrib_true(data)
    nr_occ_distrib_notok = get_number_of_occ_where_distrib_false(data)
    nr_occ_distrib_unknown = get_number_of_occ_where_distrib_unknown(data)

    nr_occ_deriv_ok = get_number_of_occ_where_deriv_true(data)
    nr_occ_deriv_notok = get_number_of_occ_where_deriv_false(data)
    nr_occ_deriv_unknown = get_number_of_occ_where_deriv_unknown(data)

    nr_occ_commer_ok = get_number_of_occ_where_commer_true(data)
    nr_occ_commer_notok = get_number_of_occ_where_commer_false(data)
    nr_occ_commer_unknown = get_number_of_occ_where_commer_unknown(data)

    nr_occ_attrib_notok = get_number_of_occ_where_attrib_true(data)
    nr_occ_attrib_ok = get_number_of_occ_where_attrib_false(data)
    nr_occ_attrib_unknown = get_number_of_occ_where_attrib_unknown(data)

    nr_occ_share_notok = get_number_of_occ_where_share_true(data)
    nr_occ_share_ok = get_number_of_occ_where_share_false(data)
    nr_occ_share_unknown = get_number_of_occ_where_share_unknown(data)

    nr_occ_notific_notok = get_number_of_occ_where_notific_true(data)
    nr_occ_notific_ok = get_number_of_occ_where_notific_false(data)
    nr_occ_notific_unknown = get_number_of_occ_where_notific_unknown(data)

    color_occ_ok = '#27AE60'
    color_occ_notok = '#CCCCCC'
    color_occ_unknown = '#C0392B'

    label_occ_ok = 'Open'
    label_occ_notok = 'Restricted/Required'
    label_occ_unknown = 'Unclear'

    label_occ_use = 'Use'
    label_occ_distrib = 'Distribution'
    label_occ_deriv = 'Derivatives'
    label_occ_commer = 'Commercial'
    label_occ_attrib = 'Attribution'
    label_occ_share = 'Share alike'
    label_occ_notific = 'Notification'

    results_json = [
    {'color': color_occ_ok, 'key': label_occ_ok, 'values': [
        {'label': label_occ_use, 'value': int(nr_occ_use_ok)},
        {'label': label_occ_distrib, 'value': int(nr_occ_distrib_ok)},
        {'label': label_occ_deriv, 'value': int(nr_occ_deriv_ok)},
        {'label': label_occ_commer, 'value': int(nr_occ_commer_ok)},
        {'label': label_occ_attrib, 'value': int(nr_occ_attrib_ok)},
        {'label': label_occ_share, 'value': int(nr_occ_share_ok)},
        {'label': label_occ_notific, 'value': int(nr_occ_notific_ok)}
    ]},
    {'color': color_occ_unknown, 'key': label_occ_unknown, 'values': [
        {'label': label_occ_use, 'value': int(nr_occ_use_unknown)},
        {'label': label_occ_distrib, 'value': int(nr_occ_distrib_unknown)},
        {'label': label_occ_deriv, 'value': int(nr_occ_deriv_unknown)},
        {'label': label_occ_commer, 'value': int(nr_occ_commer_unknown)},
        {'label': label_occ_attrib, 'value': int(nr_occ_attrib_unknown)},
        {'label': label_occ_share, 'value': int(nr_occ_share_unknown)},
        {'label': label_occ_notific, 'value': int(nr_occ_notific_unknown)}
    ]},
    {'color': color_occ_notok, 'key': label_occ_notok, 'values': [
        {'label': label_occ_use, 'value': int(nr_occ_use_notok)},
        {'label': label_occ_distrib, 'value': int(nr_occ_distrib_notok)},
        {'label': label_occ_deriv, 'value': int(nr_occ_deriv_notok)},
        {'label': label_occ_commer, 'value': int(nr_occ_commer_notok)},
        {'label': label_occ_attrib, 'value': int(nr_occ_attrib_notok)},
        {'label': label_occ_share, 'value': int(nr_occ_share_notok)},
        {'label': label_occ_notific, 'value': int(nr_occ_notific_notok)}
    ]}
    ]
    return results_json

#----------------------------
# Methods for printing html
#----------------------------
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

#----------------------------
# Main method
#----------------------------

def main():
    infile_annotated_datasets, infile_annotated_datasets_gbif_dua = sys.argv[1:]
    data = get_data(infile_annotated_datasets)
    total_oc = get_total_nr_of_occurrences(data)
    nr_oc_std_lic = nr_of_occurrences_with_standard_license(data)
    nr_oc_no_std_lic = total_oc - nr_oc_std_lic
    license_data = [{'label': 'Standard license', 'value': int(nr_oc_std_lic), 'color': '#27AE60'}, {'label': 'Non-standard license', 'value': int(nr_oc_no_std_lic), 'color': '#CCCCCC'}]
    outfile = open('charts/data/standard-license-occurrences.json', 'w+')
    outfile.write(json.dumps(license_data))
    outfile.close()

    total_nr_ds = get_total_nr_of_datasets(data)
    nr_ds_std_lic = get_nr_of_datasets_with_standard_license(data)
    nr_ds_no_std_lic = total_nr_ds - nr_ds_std_lic
    license_data = [{'label': 'Standard license', 'value': int(nr_ds_std_lic), 'color': '#27AE60'}, {'label': 'Non-standard license', 'value': int(nr_ds_no_std_lic), 'color': '#CCCCCC'}]
    outfile = open('charts/data/standard-license-datasets.json', 'w+')
    outfile.write(json.dumps(license_data))
    outfile.close()

    analysis_json = analyse_parameters_per_dataset(data)
    outfile = open('charts/data/parameters-per-dataset.json', 'w+')
    outfile.write(json.dumps(analysis_json))
    outfile.close()

    analysis_json = analyse_parameters_per_occurrence(data)
    outfile = open('charts/data/parameters-per-occurrence.json', 'w+')
    outfile.write(json.dumps(analysis_json))
    outfile.close()

    data = get_data(infile_annotated_datasets_gbif_dua)

    analysis_json = analyse_parameters_per_dataset(data)
    outfile = open('charts/data/parameters-per-dataset-gbif-dua.json', 'w+')
    outfile.write(json.dumps(analysis_json))
    outfile.close()

    analysis_json = analyse_parameters_per_occurrence(data)
    outfile = open('charts/data/parameters-per-occurrence-gbif-dua.json', 'w+')
    outfile.write(json.dumps(analysis_json))
    outfile.close()

main()
