import pandas as pd

# Loading the dataset
# Original link: https://catalog.data.gov/dataset/nchs-teen-birth-rates-for-females-by-age-group-race-and-hispanic-origin-united-states
datalink = 'https://data.cdc.gov/api/views/e8kx-wbww/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(datalink)
print(df)

df.size
df.sample(5)

# Saving as CSV file to model_dev2/data/raw
df.to_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/raw/female_teen_birth_rates.csv', index=False)

# Saving as Pickle file to model_dev2/data/raw
df.to_pickle('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/raw/female_teen_birth_rates.pkl')