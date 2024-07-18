# EUBUCCO v0.1 analysis

This repo aims to analyze EUBUCCO v0.1 to inform cleaning and downstream applications.

## Features

### Automated systematic analysis of the entire stock

One main feature is to create automated factsheets for every country. These enable us to have an overview of what is available in EUBUCCO, how it compares to [Microsoft ML Buildings](https://github.com/microsoft/GlobalMLBuildingFootprints), how reliable seems to be our data, where there seems to be issues, etc. The factsheets are currently built using EUBUCCO's [city-level overviews](/overviews) and are located [here](factsheets).

### Gathering qualitative insights from EUBUCCO users

A second main feature of this collaborative repo is that any user of EUBUCCO is invited to contribute the insights they have gathered through their interaction with the data. 

### Transparency about the data quality

The repo also aims to transparently share with all users the existing limitations of the dataset that are important to be aware of for downstream usage. 

## Contributing

To contribute, please fork the repo, commit some changes to the Markdown files / add images (images of issues go [here](imgs/issues) with the name ``<country>_<issue>.<format>``), and make a PR.

### Documenting your qualitative insights

Please add any issue you came across while using the EUBUCCO data in the Known Issues section of a country factsheet ([example](https://github.com/ai4up/eubucco-analysis/blob/main/factsheets/austria_analysis.md#known-issues)), following the template. 

### Suggest cleaning recommendations

What cleaning steps could we undertake to fix the data? Leave your ideas in the [Recommandations](https://github.com/ai4up/eubucco-analysis/blob/main/factsheets/austria_analysis.md#recommendations) section.

### Suggest additions to the automated analysis 

What other metrics would be interesting to carry out? Shoot me an email at milojevic@mcc-berlin.net. 



