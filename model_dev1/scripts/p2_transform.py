import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

# Getting the raw dataset
df = pd.read_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev1/scripts/data/popular_data_names.pkl')
print(df)

# Getting the column names
df.columns

# Cleaning the column names
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_').str.replace('(', '').str.replace(')', '')
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

