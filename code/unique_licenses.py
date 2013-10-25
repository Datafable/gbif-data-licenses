#!/usr/bin/python

import sys
import csv
import re
import os

def check_arguments():
    if len(sys.argv) != 3:
	print "usage: ./unique_licenses.py <input file> <output file>"
	print "    The input file should contain two fields: <dataset id> and <license>"
	print "    This script will read in the input, fetch all licenses and compile a"
	print "    unique list of them. The licenses will be printed out in Markdown that"
	print "    allows manual annotation. As generating a file and then manually editing"
	print "    the result can be tricky (because a second run could overwrite manual"
	print "    work), this script will first check for the presence of licenses in the"
	print "    outputfile. It will only append new licenses to the outputfile."
	sys.exit(-1)
    return sys.argv[1:]

def get_unique_input_licenses(infile_name):
    csvreader = csv.reader(open(infile_name))
    input_licenses = []
    for row in csvreader:
	ds_key, license = row
	if not license in input_licenses:
	    input_licenses.append(license)
    print "number of unique licenses: {0}".format(len(input_licenses))
    return input_licenses

def get_known_licenses(outfile_name):
    known_licenses = []
    if os.path.exists(outfile_name):
	mdreader = open(outfile_name)
	table_header = mdreader.next()
	table_dashes = mdreader.next()
	for license_line in mdreader:
	    match = re.findall('\|[^\|]+\|', license_line)[0]
	    license = match.replace('|', '')
	    known_licenses.append(license)
	mdreader.close()
    return known_licenses

def find_new_licenses(in_licenses, known_licenses):
    new_licenses = []
    for license in in_licenses:
	if not license in known_licenses:
	    new_licenses.append(license)
    return new_licenses

def write_outfile_header(outfile_name):
    writer = open(outfile_name, 'w')
    writer.write('|license|attr1|attr2|attr3|\n')
    writer.write('|-------|-----|-----|-----|\n')
    writer.close()

def append_licenses(licenses_to_append, outfile_name):
    outwriter = open(outfile_name, 'a')
    for license in licenses_to_append:
	outwriter.write('|{0}|[ ]|[ ]|[ ]|\n'.format(license))
    outwriter.close()

def main():
    infile_name, outfile_name = check_arguments()
    in_licenses = get_unique_input_licenses(infile_name)
    known_licenses = get_known_licenses(outfile_name)
    if known_licenses == []:
	print 'No licenses written in the provided output file.'
	print 'Creating the header of the outputfile now.'
	write_outfile_header(outfile_name)
    new_licenses = find_new_licenses(in_licenses, known_licenses)
    if not new_licenses == []:
	print 'Appending new licenses to the outputfile.'
	append_licenses(new_licenses, outfile_name)
    else:
	print 'All licenses of the input file were already documented'
	print 'in the provided output file.'

main()
