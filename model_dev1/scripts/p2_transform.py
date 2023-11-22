import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

# Getting the raw dataset
df = pd.read_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev1/scripts/data/popular_data_names.pkl')
df

# Getting the column names
df.columns

## Clean columns, make columns all lower case and removing white spaces
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

# Getting the data type
df.dtypes

# Keeping columns
to_keep = [
    'year_of_birth',
    'gender',
    'ethnicity',
    "child's_first_name",
    'count'
]

df = df[to_keep]
df.dropna(inplace=True)

# Performing ordinal encoding on gender
enc = OrdinalEncoder()
enc.fit(df[['gender']])
df['gender'] = enc.transform(df[['gender']])

## create dataframe with mapping for gender
df_mapping_gender = pd.DataFrame(enc.categories_[0], columns=['gender'])
df_mapping_gender['gender_ordinal'] = df_mapping_gender.index
df_mapping_gender

## save mapping to csv
df_mapping_gender.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev1/data/processed/mapping_gender.csv', index=False)

## perform ordinal encoding on "child's_first_name"
enc = OrdinalEncoder()
enc.fit(df[["child's_first_name"]])
df["child's_first_name"] = enc.transform(df[["child's_first_name"]])

df_mapping_date = pd.DataFrame(enc.categories_[0], columns=["child's_first_name"])
df_mapping_date["child's_first_name_ordinal"] = df_mapping_date.index
df_mapping_date

# Saving the mapping as a CSV for year_of_birth
df_mapping_date.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev1/data/processed/mapping_childs_first_name_ordinal.csv', index=False)

# Performing ordinal encoding on ethnicity
enc = OrdinalEncoder()
enc.fit(df[['ethnicity']])
df['ethnicity'] = enc.transform(df[['ethnicity']])

df_mapping_date = pd.DataFrame(enc.categories_[0], columns=['ethnicity'])
df_mapping_date['ethnicity_ordinal'] = df_mapping_date.index
df_mapping_date

# Saving the mapping as a CSV for ethnicity
df_mapping_date.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev1/data/processed/mapping_ethnicity.csv', index=False)

# Saving the mapping as a CSV for both ethnicity and year_of_birth
df.to_csv('model_dev1/data/processed/popular_data_names.csv', index=False)
