data/generated/datasets.csv: code/get_licenses.py
	./code/get_licenses.py > data/generated/datasets.csv

data/licenses.csv: data/generated/datasets.csv code/unique_licenses.py
	./code/unique_licenses.py data/generated/datasets.csv data/licenses.csv

data/generated/datasets-annotated.csv: data/generated/datasets.csv data/licenses.csv code/join_licenses_data.py
	./code/join_licenses_data.py data/generated/datasets.csv data/licenses.csv data/generated/datasets-annotated.csv

analysis: code/analyse.py data/generated/datasets-annotated.csv data/standard-licenses.csv
	./code/analyse.py data/generated/datasets-annotated.csv data/standard-licenses.csv

clean: 
	rm data/generated/*

all: analysis
	echo "run all rules"
