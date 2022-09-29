# Testing Data Pipelines
Using Great expectations to Test Data Pipelines

Install libraries:
```
conda install pandas
conda install -c conda-forge great-expectations
```

Dataset: [Titanic Dataset](https://www.openml.org/search?type=data&sort=runs&id=40945&status=active).

Other useful sites:
* https://greatexpectations.io/expectations/
* https://pulipulichen.github.io/jieba-js/weka/arff2csv/
* https://medium.com/towards-data-science/how-to-test-pandas-etl-data-pipeline-e49fb5dac4ce
* https://learn.microsoft.com/en-us/azure/databricks/workflows/delta-live-tables/delta-live-tables-quickstart
* [Tutorial for unit testing on Great Expectations](https://www.comet.com/standardizing-experiment/hackernews-data-expectations/reports/unit-test-your-data-with-great-expectations)

Init Great Expectations folder to generate Data Docs:
```
great_expectations init
great_expectations docs build --site-name local_site
```