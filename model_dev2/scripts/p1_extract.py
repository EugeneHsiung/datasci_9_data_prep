import pandas as pd

# Loading the dataset
# Original link: https://catalog.data.gov/dataset/2012-sat-results/resource/d6de35c7-7c4a-4b61-9fa1-232cba5d80af
datalink = 'https://data.cdc.gov/api/views/e8kx-wbww/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(datalink)
print(df)

df.size
df.sample(5)

# Saving as CSV file to model_dev2/data/raw
df.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/raw/female_teen_birth_rates.csv', index=False)

# Saving as Pickle file to model_dev2/data/raw
df.to_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/raw/female_teen_birth_rates.pkl')