import pandas as pd 

## get data 

# original link: https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1/resource/3e3345d3-5759-445c-aa2f-9bfc6891bd6b 
# data download link: 
datalink = 'https://data.cdc.gov/api/views/9j2v-jamp/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)


## save as csv to datasets/raw
df.to_csv('datasets/death_rate.csv', index=False)

## save as pickle to datasets/raw
df.to_pickle('datasets/death_rate.pkl')
