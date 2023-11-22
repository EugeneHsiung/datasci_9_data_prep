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

## Getting data types
df.dtypes

