import pandas as pd

covid_file_path = './data/owid-covid-data.csv'
# covid_file_path = './data/data_bar.csv'
df = pd.read_csv(covid_file_path, sep='|', endocing='euc-kr')
# print(df)
print(type(df))


