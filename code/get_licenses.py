#!/usr/bin/python
import requests
import json
import ast

def parse_dataset_metadata(dataset):
    if 'rights' in dataset.keys():
	rights = dataset['rights']
    else:
	rights = 'not supplied'
    return {'dataset_key': dataset['key'], 'rights': rights}

def get_gbif_datasets(limit, offset):
    params = {'limit': limit, 'offset': offset}
    r = requests.get('http://api.gbif.org/v0.9/dataset/', params=params)
    request_result = r.json()['results']
    return request_result

results = []
more_results_to_find = True
offset = 0
limit = 20
while more_results_to_find:
    datasets = get_gbif_datasets(limit, offset)
    for dataset in datasets:
	print parse_dataset_metadata(dataset)
    offset += 20
    if len(datasets) == 0:
	more_results_to_find = False

