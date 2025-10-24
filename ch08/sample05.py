import os
import pandas as pd
from matplotlib import pyplot as plt

def get_covid_data(iso_code):
    file_path = './data/common_covid.csv'

    df = pd.read_csv(file_path)
    filter_df = df[df.iso_code == iso_code]
    index_df = filter_df.set_index('date')

    return index_df['total_cases']
#end-def

kor_data = get_covid_data('KOR')
usa_data = get_covid_data('USA')
fra_data = get_covid_data('FRA')
gbr_data = get_covid_data('GBR')
pol_data = get_covid_data('POL')
index_data = kor_data.index

def get_cvid_data(iso_code):
    file_path = './data/common_covid.csv'

    df = pd.read_csv(file_path)

    common_population_sr = df[df.iso_code == 'USA']['population']
    print('common population:', common_population_sr)

    filter_df = df[df.iso_code == iso_code]

    rate = 1

a = round(usa_data / kor_data, 2)
b = round(usa_data / fra_data, 2)
c = round(usa_data / gbr_data, 2)
d = round(usa_data / pol_data, 2)

covid_df = pd.DataFrame(
    {
    'KOR': kor_data * a,
    'USA': usa_data,
    'FRA': fra_data * b,
    'GBR': gbr_data * c,
    'POL': pol_data * d,
}, index = index_data)
covid_df[:].plot.line(rot = 45)
plt.show()


