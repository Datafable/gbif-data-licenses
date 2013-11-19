#!/usr/bin/python

import sys
import csv

def check_arguments():
    if len(sys.argv) != 3:
	print 'usage: ./reinterpret_no_license.py <annotated licenses file> <new output file>'
	sys.exit(-1)
    return sys.argv[1:]

def get_input(infile):
    lines = []
    with open(infile) as f:
	reader = csv.reader(f, delimiter=',')
        header = reader.next()
	for line in reader:
	    lines.append(line)
    return [header, lines]

def reinterpret_no_license(input_lines):
    reinterpreted_lines = []
    for line in input_lines:
	std_lic, use, distrib, deriv, commerc, attrib, share, notif, license = line
	if license == '':
	    std_lic = ''
	    use = 'true'
	    distrib = 'true'
	    deriv = 'true'
	    commerc = '?'
	    attrib = 'true'
	    share = '?'
	    notif = 'false'
	    line = [std_lic, use, distrib, deriv, commerc, attrib, share, notif, license]
	reinterpreted_lines.append(line)
    return reinterpreted_lines

def write_output(header, lines, outfile):
    with open(outfile, 'w+') as f:
        wr = csv.writer(f, delimiter=',')
        wr.writerow(header)
	for line in lines:
	    wr.writerow(line)

def main():
    infile, outfile = check_arguments()
    input_header, input_lines = get_input(infile)
    reinterpreted_lines = reinterpret_no_license(input_lines)
    write_output(input_header, reinterpreted_lines, outfile)

main()
