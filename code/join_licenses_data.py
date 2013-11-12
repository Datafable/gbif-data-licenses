#!/usr/bin/python

import sys
import csv

def check_arguments():
    if len(sys.argv) != 4:
	print 'usage: ./join_licenses_data.py <datasets_file> <licenses_file> <outfile>'
	sys.exit(-1)
    return sys.argv[1:]

def read_annotated_licenses(infile):
    licenses = {}
    with open(infile) as f:
        reader = csv.reader(f, delimiter=',')
	header = reader.next()
	for row in reader:
	    annotations = row[0:8]
	    license_text = row[8]
	    licenses[license_text] = annotations
    return licenses

def read_datasets(infile):
    datasets = []
    with open(infile) as f:
        reader = csv.reader(f, delimiter=',')
	header = reader.next()
	for row in reader:
	    datasets.append(row)
    return datasets

def write_annotation_per_dataset(datasets_list, ann_licenses_dict, outfile):
    with open(outfile, 'w+') as f:
	writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['key','owningOrganizationKey','numberOfOccurrences','rights','standard license','use','distribution','derivatives','commercial','attribution','share alike','notification'])
	for dataset in datasets_list:
	    license = dataset[-1]
	    license_annotations = ann_licenses_dict[license]
	    writer.writerow(dataset + license_annotations)
    return True

def main():
    datasets_file, licenses_file, outfile = check_arguments()
    ann_licenses = read_annotated_licenses(licenses_file)
    datasets = read_datasets(datasets_file)
    write_annotation_per_dataset(datasets, ann_licenses, outfile)

main()
