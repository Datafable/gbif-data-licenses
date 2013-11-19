data/generated/datasets.csv: code/get_licenses.py
	./code/get_licenses.py > data/generated/datasets.csv

data/licenses.csv: data/generated/datasets.csv code/unique_licenses.py
	./code/unique_licenses.py data/generated/datasets.csv data/licenses.csv

data/generated/licenses-gbif-dua.csv: data/licenses.csv
	./code/reinterpret_no_license.py data/licenses.csv data/generated/licenses-gbif-dua.csv

data/generated/datasets-annotated.csv: data/generated/datasets.csv data/licenses.csv code/join_licenses_data.py
	./code/join_licenses_data.py data/generated/datasets.csv data/licenses.csv data/generated/datasets-annotated.csv

data/generated/datasets-annotated-gbif-dua.csv: data/generated/datasets.csv data/generated/licenses-gbif-dua.csv code/join_licenses_data.py
	./code/join_licenses_data.py data/generated/datasets.csv data/generated/licenses-gbif-dua.csv data/generated/datasets-annotated-gbif-dua.csv
