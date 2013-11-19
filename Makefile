data/datasets.csv: code/get_licenses.py
	./code/get_licenses.py > data/datasets.csv

data/licenses.csv: data/datasets.csv code/unique_licenses.py
	./code/unique_licenses.py ./data/datasets.csv ./data/licenses.csv

data/licenses-gbif-dua.csv: data/licenses.csv
	./code/reinterpret_no_license.py data/licenses.csv data/licenses-gbif-dua.csv

data/datasets-annotated.csv: data/datasets.csv data/licenses.csv code/join_licenses_data.py
	./code/join_licenses_data.py data/datasets.csv data/licenses.csv data/datasets-annotated.csv

data/datasets-annotated-gbif-dua.csv: data/datasets.csv data/licenses-gbif-dua.csv code/join_licenses_data.py
	./code/join_licenses_data.py data/datasets.csv data/licenses-gbif-dua.csv data/datasets-annotated-gbif-dua.csv

analysis: code/analyse.py data/datasets-annotated.csv data/datasets-annotated-gbif-dua.csv
	./code/analyse.py data/datasets-annotated.csv data/datasets-annotated-gbif-dua.csv
