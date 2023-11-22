# datasci_9_data_prep

[Assignment 9](https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/assignment9.md): Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

### Dataset # 1: [Popular_Baby_Names](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/Datasets/Popular_Baby_Names.csv)
+ This dataset contains: Popular Baby Names by Sex and Ethnic Group Data were collected through civil birth registration. Each record represents the ranking of a baby name in the order of frequency. Data can be used to represent the popularity of a name.
+ The intended machine learning task for this dataset is classification
+ The steps for data cleaning and transforming are shown in each `p2 file` under scripts in each [Model 1](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/model_dev1/scripts/p2_transform.py) and [Model 2](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/model_dev2/scripts/p2_transform.py).

Examples of cleaning: 

```
## Clean columns, make columns all lower case and removing white spaces
df.columns = df.columns.str.lower().str.replace(' ', '_')
```
and 
```
# keep specified columns and drop missing values
df = df[to_keep]
df.dropna(inplace=True)```

