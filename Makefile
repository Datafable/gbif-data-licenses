data/datasets.csv: code/get_licenses.py
	./code/get_licenses.py > data/datasets.csv

data/licenses.mkd: data/datasets.csv code/unique_licenses.py
	./code/unique_licenses.py ./data/datasets.csv ./data/licenses.mkd
