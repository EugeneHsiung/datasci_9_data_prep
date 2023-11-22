import pandas as pd

# Loading the dataset
# Original link: https://catalog.data.gov/dataset/popular-baby-names/resource/02e8f55e-2157-4cb2-961a-2aabb75cbc8b
datalink = 'https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(datalink)
print(df)

df.size
df.sample(5)

# Saving as CSV file to model_dev1/data/raw
df.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev1/scripts/data/popular_data_names.csv', index=False)

# Saving as Pickle file to model_dev1/data/raw
df.to_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev1/scripts/data/popular_data_names.pkl')