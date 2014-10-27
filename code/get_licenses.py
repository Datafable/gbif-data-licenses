#!/usr/bin/python
import requests
import json
import csv
import sys

def parse_dataset_metadata(dataset):
    if 'rights' in dataset.keys():
        rights = dataset['rights'].encode('utf-8').strip()
        rights = rights.replace("\n", "")
    else:
        rights = ''
    return [dataset['key'].encode('utf-8'), dataset['owningOrganizationKey'].encode('utf-8'), rights]

def get_gbif_datasets(limit, offset):
    params = {'limit': limit, 'offset': offset}
    r = requests.get('http://api.gbif.org/v1/dataset/', params=params)
    request_result = r.json()['results']
    return request_result

def getOccurrences(key):
    params = {'datasetKey':  key}
    r = requests.get('http://api.gbif.org/v1/occurrence/count', params=params)
    try:
        count = r.json()
    except:
        sys.stderr.write('could not parse json for number of occurrences for key {0}\n'.format(key))
        sys.exit(-1)
    return count

all_datasets = []
more_results_to_find = True
offset = 0
limit = 20
print 'key,owningOrganizationKey,numberOfOccurrences,rights'
csvwriter = csv.writer(sys.stdout, lineterminator='\n')

while more_results_to_find:
    #sys.stderr.write('LOG: calling GBIF')
    datasets = get_gbif_datasets(limit, offset)
    all_datasets += datasets
    offset += 20
    if len(datasets) == 0:
        more_results_to_find = False

for dataset in all_datasets:
    dataset_list = parse_dataset_metadata(dataset)
    key = dataset_list[0]
    count = getOccurrences(key)
    dataset_list.insert(2, count)
    csvwriter.writerow(dataset_list)
