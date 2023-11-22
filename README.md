# datasci_9_data_prep

[Assignment 9](https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/assignment9.md): Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

### Dataset # 1: [Popular_Baby_Names](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/Datasets/Popular_Baby_Names.csv)
+ This dataset contains: Popular Baby Names by Sex and Ethnic Group Data were collected through civil birth registration. Each record represents the ranking of a baby name in the order of frequency. Data can be used to represent the popularity of a name. More information can be found [here](https://catalog.data.gov/dataset/popular-baby-names)
+ The intended machine-learning task for this dataset is classification
+ The steps for data cleaning and transforming are shown in `p2 file` under scripts in [Model 1](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/model_dev1/scripts/p2_transform.py)  
Examples of cleaning: 

```
## Clean columns, make columns all lower case and removing white spaces
df.columns = df.columns.str.lower().str.replace(' ', '_')
```
and 
```
# keep specified columns and drop missing values
df = df[to_keep]
df.dropna(inplace=True)
```
+ Dependent variable: child's_first_name, Independent variables: gender and ethnicity
+ All variables underwent ordinal cleaning and were saved as a CSV in the [processed folder](https://github.com/EugeneHsiung/datasci_9_data_prep/tree/main/model_dev1/data/processed)


### Dataset # 2: [Teen_Birth_Rates_for_Females](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/Datasets/NCHS_-_Teen_Birth_Rates_for_Females_by_Age_Group__Race__and_Hispanic_Origin__United_States.csv)
+ This dataset contains: This dataset includes teen birth rates for females by age group, race, and Hispanic origin in the United States since 1960. More information can be found [here](https://catalog.data.gov/dataset/nchs-teen-birth-rates-for-females-by-age-group-race-and-hispanic-origin-united-states)
+ The intended machine-learning task for this dataset is classification
+ The steps for data cleaning and transforming are shown in `p2 file` under scripts in [Model 2](https://github.com/EugeneHsiung/datasci_9_data_prep/blob/main/model_dev2/scripts/p2_transform.py)
+ The same cleaning examples listed for Model 1 were used in Model 2
+  Dependent variable: birth_rate, Independent variables: race_or_hispanic_origin and age_group
+  All variables underwent ordinal cleaning and were saved as a CSV in the [processed folder](https://github.com/EugeneHsiung/datasci_9_data_prep/tree/main/model_dev2/data/processed) 

