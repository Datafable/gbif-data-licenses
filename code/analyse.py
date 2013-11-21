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
    #print 'total number of occurrences: {0}'.format(total_sum)
    return total_sum

def get_total_nr_of_datasets(data):
    total = len(data)
    return total

def get_nr_of_datasets_with_no_license(data):
    subset = data[data['rights'].isnull()]
    return len(subset)

def get_nr_of_datasets_with_standard_license(data):
    subset = data[data['standard license'].notnull()]
    return len(subset)

def nr_of_occurrences_with_no_license(data):
    subset = data[data['rights'].isnull()]
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    #print 'number of occurrences with no license: {0}'.format(subset_sum)
    return subset_sum

def nr_of_occurrences_with_standard_license(data):
    subset = data[data['standard license'].notnull()]
    subset_sum = subset['numberOfOccurrences'].apply(int).sum()
    #print 'number of occurrences with standard licenses: {0}'.format(subset_sum)
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
# Output methods
#----------------------------
def dataframe_to_markdown(df, indexname):
    header_line = '|' + indexname + '|' + '|'.join(df.columns) + '|'
    sep_list = []
    for i in range(len(df.columns) + 1):
        sep_list.append('----')
    sep_line = '|' + '|'.join(sep_list) + '|'
    data_lines = []
    for rowname in df.index:
        line = '|' + rowname + '|' + '|'.join([str(df[x][rowname]) for x in df.columns]) + '|'
        data_lines.append(line)
    return '\n'.join([header_line, sep_line] + data_lines)

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
    color_ds_notok = '#C0392B'
    color_ds_unknown = '#CCCCCC'

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
    color_occ_notok = '#C0392B'
    color_occ_unknown = '#CCCCCC'

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

def analyse_std_license(data, std_licenses_data):
    joined_data = pd.merge(data, std_licenses_data, how='left', left_on='standard license', right_on='url')
    agg = joined_data.groupby('code')
    occurrences_with_std_licenses = agg['numberOfOccurrences'].sum()
    datasets_with_std_licenses = agg.size()
    index = occurrences_with_std_licenses.index
    table = pd.DataFrame({'# of datasets': datasets_with_std_licenses, '# of records': occurrences_with_std_licenses}, index=index)
    total_oc = get_total_nr_of_occurrences(data)
    total_nr_ds = get_total_nr_of_datasets(data)
    nr_oc_std_lic = nr_of_occurrences_with_standard_license(data)
    nr_oc_no_lic = nr_of_occurrences_with_no_license(data)
    nr_oc_no_std_lic = total_oc - nr_oc_std_lic - nr_oc_no_lic
    nr_ds_std_lic = get_nr_of_datasets_with_standard_license(data)
    nr_ds_no_lic = get_nr_of_datasets_with_no_license(data)
    nr_ds_no_std_lic = total_nr_ds - nr_ds_std_lic - nr_ds_no_lic
    no_license_row = pd.DataFrame({'# of datasets': nr_ds_no_lic, '# of records': nr_oc_no_lic}, index=['no license'])
    no_std_license_row = pd.DataFrame({'# of datasets': nr_ds_no_std_lic, '# of records': nr_oc_no_std_lic}, index=['no standard license'])
    outtable = pd.concat([table, no_license_row, no_std_license_row])
    outtable['% of occurrence records'] = outtable['# of records'] / float(total_oc)
    return outtable

#----------------------------
# Main method
#----------------------------

def main():
    infile_annotated_datasets, std_license_doc = sys.argv[1:]
    data = get_data(infile_annotated_datasets)
    std_licenses_data = get_data(std_license_doc)
    total_oc = get_total_nr_of_occurrences(data)
    nr_oc_std_lic = nr_of_occurrences_with_standard_license(data)
    nr_oc_no_std_lic = total_oc - nr_oc_std_lic
    std_lic_occ_data = [{'label': 'Standard license', 'value': int(nr_oc_std_lic), 'color': '#27AE60'}, {'label': 'Non-standard license', 'value': int(nr_oc_no_std_lic), 'color': '#CCCCCC'}]

    total_nr_ds = get_total_nr_of_datasets(data)
    nr_ds_std_lic = get_nr_of_datasets_with_standard_license(data)
    nr_ds_no_std_lic = total_nr_ds - nr_ds_std_lic
    std_lic_dataset_data = [{'label': 'Standard license', 'value': int(nr_ds_std_lic), 'color': '#27AE60'}, {'label': 'Non-standard license', 'value': int(nr_ds_no_std_lic), 'color': '#CCCCCC'}]

    param_ds_data = analyse_parameters_per_dataset(data)
    param_occ_data = analyse_parameters_per_occurrence(data)

    outfile = open('charts/js/data.js', 'w+')
    outfile.write('var std_license_occ_data = {0};\n\n'.format(json.dumps(std_lic_occ_data)))
    outfile.write('var std_license_ds_data = {0};\n\n'.format(json.dumps(std_lic_dataset_data)))
    outfile.write('var params_ds_data = {0};\n\n'.format(json.dumps(param_ds_data)))
    outfile.write('var params_occ_data = {0};\n\n'.format(json.dumps(param_occ_data)))
    outfile.close()

    std_license_data = analyse_std_license(data, std_licenses_data)
    f = open('data/generated/standard-license-data.csv', 'w+')
    std_license_data.to_csv(f, sep=',', header=True, index=True, index_label='License', float_format='%.6f')
    f.close()

main()
