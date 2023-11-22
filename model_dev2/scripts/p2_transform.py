import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

# Getting the raw dataset
df = pd.read_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/raw/female_teen_birth_rates.pkl')
df

## Getting column names
df.columns

## Clean columns, make columns all lower case and removing white spaces
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

## data types
df.dtypes

# Keep all columns 
to_keep = [
    'year',
    'race_or_hispanic_origin',
    'age_group',
    'birth_rate',
]

# keep specified columns and drop missing values
df = df[to_keep]
df.dropna(inplace=True)

# Performing ordinal encoding on age_group
enc = OrdinalEncoder()
enc.fit(df[['age_group']])
df['age_group'] = enc.transform(df[['age_group']])

## create dataframe with mapping for age_group
df_mapping_age_group = pd.DataFrame(enc.categories_[0], columns=['age_group'])
df_mapping_age_group['age_group_ordinal'] = df_mapping_age_group.index
df_mapping_age_group

## save age_group to csv
df_mapping_age_group.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/processed/mapping_age_group.csv', index=False)

## perform ordinal encoding on race_or_hispanic_origin
enc = OrdinalEncoder()
enc.fit(df[['race_or_hispanic_origin']])
df['race_or_hispanic_origin'] = enc.transform(df[['race_or_hispanic_origin']])

## create dataframe with mapping for race_or_hispanic_origin
df_mapping_race_or_hispanic_origin = pd.DataFrame(enc.categories_[0], columns=['race_or_hispanic_origin'])
df_mapping_race_or_hispanic_origin['race_or_hispanic_origin'] = df_mapping_race_or_hispanic_origin.index
df_mapping_race_or_hispanic_origin

## save mapping to csv
df_mapping_race_or_hispanic_origin.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/processed/mapping_race_or_hispanic_origin.csv', index=False)

## perform ordinal encoding on birth_rate
enc = OrdinalEncoder()
enc.fit(df[['birth_rate']])
df['birth_rate'] = enc.transform(df[['birth_rate']])

## create dataframe with mapping for birth_rate
df_mapping_birth_rate = pd.DataFrame(enc.categories_[0], columns=['birth_rate'])
df_mapping_birth_rate['birth_rate'] = df_mapping_birth_rate.index
df_mapping_birth_rate

## save mapping to csv
df_mapping_birth_rate.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/processed/mapping_birth_rate.csv', index=False)


## Save in processed folder
df.to_csv('model_dev2/data/processed/processed_female_teen_birth_rate.csv', index=False)