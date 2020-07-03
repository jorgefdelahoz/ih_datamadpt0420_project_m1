# General libs
import pandas as pd
from functools import reduce
import requests
# Libs used with DDBB
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
# Libs used with API
import json
# Libs used with Web Scrapping
from bs4 import BeautifulSoup
import re



def get_engine_db(path):
    print(f'...starting connection with database...')
    engine = create_engine(f'sqlite:///{path}', poolclass=StaticPool)
    df_personal_info = pd.read_sql_table(table_name='personal_info', con=engine)
    df_career_info = pd.read_sql_table(table_name='career_info', con=engine)
    df_country_info = pd.read_sql_table(table_name='country_info', con=engine)
    df_poll_info = pd.read_sql_table(table_name='poll_info', con=engine)
    df_database_merge = reduce(lambda left_table, right_table : pd.merge(left_table, right_table, on='uuid'),
                               [df_personal_info,df_career_info,df_country_info,df_poll_info])
    df_database_merge.to_csv('./data/raw/raw_df_database_merge.csv', index=False)

    return df_database_merge

def get_api_jobs(jobs):
    jobs_id = list(pd.unique(jobs['normalized_job_code']))
    jobs_id.remove(None)
    request_list = [requests.get(f'http://api.dataatwork.org/v1/jobs/{job_id}').json() for job_id in jobs_id]
    request_json = json.dumps(request_list)
    df_jobs_title = pd.read_json(request_json)
    print('Extracting API info into raw_df_jobs_title.csv...')
    df_jobs_title.to_csv('./data/raw/raw_df_jobs_title.csv', index=False)

    return df_jobs_title


def get_api_provisional(jobs):
    df_jobs_title=pd.read_csv('./data/raw/raw_df_jobs_title.csv')

    return df_jobs_title


def get_web_scrapping(countries):
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('div', {'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12 content-col content article-content'})[0]
    rows = table.find_all('td')
    rows_parsed = [row.text for row in rows]
    clean_rows = [re.sub('^\s|[()]|\n|(?:\[\\d\])|\*\s|[*]', '', i) for i in rows_parsed]
    clean_rows = [re.sub('EL', 'GR', i) for i in clean_rows]
    clean_rows = [re.sub('UK', 'GB', i) for i in clean_rows]
    clean_rows = [x for x in clean_rows if x]
    AUX = 2
    country_relationship = [clean_rows[x:x + AUX] for x in range(0, len(clean_rows), AUX)]
    df_country_relationship = pd.DataFrame(country_relationship)
    df_country_relationship_colnames = ['country', 'country_code']
    df_country_relationship.columns = df_country_relationship_colnames
    df_country_relationship.to_csv('./data/raw/raw_df_scrapping_countries.csv')

    return df_country_relationship

# USING CSVs
# def df_merge(data):
#     df_db = pd.read_csv('./data/raw/raw_df_database_merge.csv')
#     df_api = pd.read_csv('./data/raw/raw_df_jobs_title.csv')
#     df_wscrapping = pd.read_csv('./data/raw/raw_df_scrapping_countries.csv')
#     career_job_info = pd.merge(df_db, df_api, left_on='normalized_job_code', right_on='uuid', how='outer',
#                                sort=False, suffixes=('', '_y'))
#     # career_job_info = career_job_info[
#     #     ['uuid', 'dem_education_level', 'dem_full_time_job', 'normalized_job_code', 'title']]
#     df_project = pd.merge(career_job_info, df_wscrapping, left_on='country_code', right_on='country_code',
#                           how='inner', sort=False, suffixes=('', '_y'))
#
#     df_project.to_csv('./data/raw/raw_df_project_merged.csv')
#
#     return df_project


def merge_dataframes(data_db,data_api,data_wscrapping):
    # Merge dataframe extracted from database with dataframe info extracted from API
    data_merged_personal_job_info = pd.merge(data_db, data_api, left_on='normalized_job_code', right_on='uuid', how='outer',
                                sort=False, suffixes=('', '_y'))
    # Merge datamerged with dataframe info extracted from web scrapping
    data_merged_ws_job_info = pd.merge(data_merged_personal_job_info, data_wscrapping, left_on='country_code', right_on='country_code',
                          how='inner', sort=False, suffixes=('', '_y'))

    data_merged_ws_job_info = data_merged_ws_job_info.rename(columns={'question_bbi_2016wave4_basicincome_awareness':'awareness',
        'question_bbi_2016wave4_basicincome_vote':'vote', 'question_bbi_2016wave4_basicincome_effect': 'effect',
        'question_bbi_2016wave4_basicincome_argumentsfor':'arguments_for',
        'question_bbi_2016wave4_basicincome_argumentsagainst':'arguments_against'})

    return data_merged_ws_job_info

def acquire(path):
    print(f'reading data from {path}...')
    table = get_engine_db(path)
    # print(f'Data Database:\n{table}')
    api = get_api_provisional(table)
    # api = get_api_jobs(table)
    # print(f'Data API:\n{api}')
    wscrapping = get_web_scrapping(api)
    # print(f'Data WEB SCRAPPING:\n{wscrapping}')
    df_merge = merge_dataframes(table,api,wscrapping)
    # print(f'Data Merged:\n{df_merge}')
    return df_merge
