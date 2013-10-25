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
	rights = 'not supplied'
    return [dataset['key'].encode('utf-8'), rights]

def get_gbif_datasets(limit, offset):
    params = {'limit': limit, 'offset': offset}
    r = requests.get('http://api.gbif.org/v0.9/dataset/', params=params)
    request_result = r.json()['results']
    return request_result

results = []
more_results_to_find = True
offset = 0
limit = 20
print '#dataset-key,rights'
csvwriter = csv.writer(sys.stdout)
while more_results_to_find:
    datasets = get_gbif_datasets(limit, offset)
    for dataset in datasets:
	csvwriter.writerow(parse_dataset_metadata(dataset))
    offset += 20
    if len(datasets) == 0:
	more_results_to_find = False

