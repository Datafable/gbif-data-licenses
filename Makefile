data/datasets.csv: code/get_licenses.py
	./code/get_licenses.py > data/datasets.csv

data/licenses.csv: data/datasets.csv code/unique_licenses.py
	./code/unique_licenses.py ./data/datasets.csv ./data/licenses.csv

data/licenses-gbif.csv: data/licenses.csv
	./code/reinterpret_no_license.py data/licenses.csv data/licenses-gbif.csv
