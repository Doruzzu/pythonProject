import pandas as pd
import numpy as np


def df_countries():
    """ This function should return a DataFrame  and the rows of the DataFrame should be sorted by ' Rank'
    indec is : Index(['Rank', 'Region', 'Documents', 'Citable documents', 'Citations',
       'Self-citations', 'Citations per document', 'H index', 'Energy Supply',
       'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
       '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
       '2018', '2019', '2020', '2021', 'Unnamed: 66'],
      dtype='object' """
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    GDP = pd.read_csv('world_bank.csv', skiprows=4)

    Energy = pd.read_excel('Energy Indicators.xls')

    Energy = Energy[16:243]

    Energy['Unnamed: 2'] = Energy['Unnamed: 2'].str.replace(r'\s?\([A-Za-z ]+\)\s?|[0-9]+', '', regex=True)

    Energy.drop(columns=['Unnamed: 0', 'Unnamed: 1'], inplace=True)
    Energy.rename(columns={'Unnamed: 2': 'Country', 'Unnamed: 3': 'Energy Supply','Unnamed: 4': 'Energy Supply per Capita','Unnamed: 5': '% Renewable'}, inplace=True)

    Energy.replace(to_replace={'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom','Republic of Korea': "South Korea", "United States of America": "United States"},
                   inplace=True)

    Energy.reset_index(inplace=True)
    Energy.drop(columns='index', inplace=True)
    Energy['Energy Supply'].replace(to_replace={'...': np.NAN}, inplace=True)
    Energy['Energy Supply'] = Energy['Energy Supply'] * 1000000
    Energy['Country'] = Energy['Country'].str.replace(r'\s?\([A-Za-z ]+\)\s?|[0-9]+', '', regex=True)

    # GDP.drop(columns='Unnamed: 65', inplace=True)

    GDP['Country Name'].replace(
        to_replace={"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", "Hong Kong SAR, China": "Hong Kong"},
        inplace=True)

    #  pattern=r'\s?\([A-Za-z ]+\)\s?'


    drop_years = [str(year) for year in range(1960, 2006)]

    GDP.drop(columns=drop_years, inplace=True)
    new_ScimEn = ScimEn[ScimEn['Rank'] < 16]

    new_df = pd.merge(new_ScimEn, Energy, how='left', left_on='Country', right_on='Country')

    final_df = pd.merge(new_df, GDP, how='left', right_on='Country Name', left_on='Country')

    final_df.set_index('Country', drop=True, inplace=True)

    final_to_drop = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']

    final_df.drop(columns=final_to_drop, inplace=True)
    df = final_df

    return df

print(df_countries().columns)

