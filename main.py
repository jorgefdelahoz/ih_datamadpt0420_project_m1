import argparse
import time
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man

def argument_parser():
    parser = argparse.ArgumentParser(description='Specify inputs')
    parser.add_argument("-p", "--path", help="Specify .db database path", required=True, type=str)
    parser.add_argument("-c", "--country", help="Select country", type=str, default='all')
    args = parser.parse_args()
    return args


def main(arguments):

    print('starting pipeline...')
    print(f'\nTABLE:\tdf_database_merge\n-------------------')
    df_project = mac.acquire(arguments.path)

    data_merged = mwr.wrangling(df_project)
    data_merged.to_csv('./data/processed/data_merged_info.csv')

    data_project_analysed = man.analyce_data(data_merged,arguments.country)
    data_project_analysed.to_csv('./data/results/country_gender_analysed.csv')
    print(data_project_analysed)

    # Bonus 1:
    data_opinions = man.judgement(df_project)
    data_opinions.to_csv('./data/results/Bonus1-Data_Opinions.csv')
    print(data_opinions)

    print('========================= Pipeline is complete. You may find the results in the folder '
          './data/results =========================')


if __name__ == '__main__':
    main(argument_parser())