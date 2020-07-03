import re
import numpy as np
import pandas as pd

def analyce_data(df, country='all'):
    lst_groups = ['country', 'title', 'gender']
    df['Quantity'] = 0
    df = df.groupby(lst_groups).agg({'Quantity': 'count'}).reset_index()
    total = df['Quantity'].sum()
    df['Percentage'] = df['Quantity'].apply(lambda x: ("{:.3%}".format(x / total)))


    if country != 'all':
        print(f'Filtered by {country}\nExporting into csv...')
        df = df[df['country'] == country.title()]
    else:
        print('-------------------------------------------\n\t\tALL COUNTRIES SELECTED\n------------------------------'
              '-------------')
    return df

def judgement(df):
    df = df[['vote', 'arguments_for', 'arguments_against']]
    df['arguments_for'].replace('None of the above', np.nan)
    df['arguments_against'].replace('None of the above', np.nan)
    pd.set_option('mode.chained_assignment', None)
    df['arguments_for'] = df['arguments_for'].apply(lambda x: re.split('[|]', x)).apply(
        lambda x: len(x))
    df['arguments_against'] = df['arguments_against'].apply(lambda x: re.split('[|]', x)).apply(
        lambda x: len(x))
    df.vote = df.vote.apply(lambda x: 'Against' if 'against' in x else ('NA' if 'not' in x else 'In Favour'))
    df_opinions = df.groupby(['vote']).sum().reset_index()
    df_opinions = df_opinions.rename(columns={'vote': 'Position',
                                              'arguments_for': 'Number of Pro Arguments',
                                              'arguments_against': 'Number of Cons Arguments'})

    return df_opinions

