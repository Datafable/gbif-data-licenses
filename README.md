# GBIF data licenses

## Rationale

Data publishers of the [Global Biodiversity Information Facility](http://www.gbif.org) (GBIF) apply a wide range of licenses to their datasets. This is [problematic](http://peterdesmet.com/posts/illegal-bullfrogs.html):

* Users of the data need to investigate and understand those licenses before they can use the data.
* Many licenses don't comply with the practices of GBIF and/or open data, limiting the use of the data.

## Goal

We want to get an overview of the characteristics of the licenses used in all GBIF registered datasets.

## Results

1. Metadata of all datasets is obtained via the [GBIF Registry API](http://www.gbif.org/developer/registry) and written to [datasets.csv](data/generated/datasets.csv). `make data/generated/datasets.csv`
2. All unique licenses are written to [licenses.csv](data/licenses.csv). Rerunning the scripts will append newly found licenses to the file. `make data/licenses.csv`
3. The [characteristics of the licenses](data/licenses.csv) are manually interpreted using [these guidelines](guidelines.md).
4. The annotated information is merged with the [datasets](data/generated/datasets-annotated.csv)†. `make data/generated/datasets-annotated.csv`
5. These data are analyzed. `make analysis`
6. The results are written to [standard-license-data.csv](data/generated/standard-license-data.csv) and [data.js](charts/js/data.js).
7. The latter is used as the basis for [charts](charts/), which are [displayed](http://datafable.com/gbif-data-licenses/charts/index.html) from the `gh-pages` branch.
8. The results of the analysis were presented in [this blog post](http://peterdesmet.com/posts/analyzing-gbif-data-licenses.html).

† You can easily transform the UUID keys to working URLs as follows:

* `"http://www.gbif.org/dataset/" & key`: [http://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2](http://www.gbif.org/dataset/66f6192f-6cc0-45fd-a2d1-e76f5ae3eab2)
* `"http://www.gbif.org/publisher/" & owningOrganizationKey`: [http://www.gbif.org/publisher/1989b627-2a61-44db-83e4-392efc5da0a9](http://www.gbif.org/publisher/1989b627-2a61-44db-83e4-392efc5da0a9)

## Requirements

* Unix make
* Python
* requests
* pandas
* simplejson
* [d3](https://github.com/mbostock/d3): visualization JS library ([license](https://github.com/mbostock/d3/blob/master/LICENSE))
* [nvd3](https://github.com/novus/nvd3): charts JS Library ([license](https://github.com/novus/nvd3/blob/master/LICENSE.md)) - included
