# GBIF data licenses

## Rationale

Data publishers of the Global Biodiversity Information Facility ([GBIF](http://www.gbif.org)) apply a wide range licenses to their datasets. This is [problematic](http://peterdesmet.com/posts/illegal-bullfrogs.html):

* Users of the data need to investigate and understand those licenses before they can use the data.
* Many licenses don't comply with the practices of GBIF and/or open data, limiting the use of the data.

## Goal

We want to get an overview of all data licenses used in GBIF registered datasets and translate those to standard licenses where possible.

## Results

All licenses are written to [licenses.csv](/data/licenses.csv). Rerunning the scripts will append newly found licenses to the file.

The licenses are manually interpreted in the form of `true`/`false`/`?` parameters using [these guidelines](guidelines.md) we created.

---

## Content

* [/code](./code): scripts to fetch all data licenses.
* [/data](./data): output of the scripts and manual annotation.

Use [blame](https://github.com/blog/228-playing-the-blame-game) to find out when they were generated or edited.

## How to run the code

### Fetch all dataset metadata from GBIF

`make data/datasets.csv`

This command will fetch all metadata from GBIF datasets and parse the dataset code and rights from it. The output will be written to the data folder.

### Add new licenses to the licenses file

`make data/licenses.csv`

This command will run the `unique_licenses.py` script. It will fetch the metadata from the `data/datasets.csv` file, look for licenses that were not documented in `data/licenses.mkd` yet, and append these to the file. If the file `data/licenses.mkd` does not exist, it will be created.

## Requirements

* Unix make
* Python
* Python modules: requests
