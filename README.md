# GBIF data licenses

## Rationale

Data publishers of the Global Biodiversity Information Facility ([GBIF](http://www.gbif.org)) apply a wide range licenses to their datasets. This is [problematic](http://peterdesmet.com/posts/illegal-bullfrogs.html):

* Users of the data need to investigate and understand those licenses before they can use the data.
* Many licenses don't comply with the practices of GBIF and/or open data, limiting the use of the data.

## Goal

We want to get an overview of all data licenses used in GBIF registered datasets and translate those to standard licenses where possible.

## Results

1. Metadata for all datasets is obtained via the [GBIF Registry API](http://www.gbif.org/developer/registry) and written to [datasets.csv](data/datasets.csv) [`make data/datasets.csv`]
2. All unique licenses are written to [licenses.csv](data/licenses.csv). Rerunning the scripts will append newly found licenses to the file. [`make data/licenses.csv`]
3. The [characteristics of the licenses](data/licenses.csv) are manually interpreted using [these guidelines](guidelines.md) we created.
4. The annotated information is added back to [the datasets](data/datasets-annotated.csv).
5. [Charts](http://datafable.github.io/gbif-data-licenses/charts/index.html) provide a visualization of the distribution of the licenses.

## Requirements

* Unix make
* Python
* requests
* pandas
* [nvd3](https://github.com/novus/nvd3): charts JS Library ([license](https://github.com/novus/nvd3/blob/master/LICENSE.md)) - included
