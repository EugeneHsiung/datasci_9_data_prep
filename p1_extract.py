import pandas as pd 

## get data 

# original link: https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1/resource/3e3345d3-5759-445c-aa2f-9bfc6891bd6b 
# data download link: 
datalink = 'https://data.cdc.gov/api/views/9j2v-jamp/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)


## save as csv to WK9/code/model_dev/data/raw
df.to_csv('WK9/code/model_dev/data/raw/crime_data.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('WK9/code/model_dev/data/raw/crime_data.pkl')


# LAPD reporting districts 
## original link: https://geohub.lacity.org/datasets/39b404bd22804807ba0f0e1628e585f2/explore