import numpy as np
import re

# In order to be able to analyze more accurately, it's necessary to make a previous data cleaning...
# Lets modify values into lowercase...
def lower_case(df):
    df['gender'] = df['gender'].str.lower()
    df['dem_has_children'] = df['dem_has_children'].str.lower()
    return df

# Replace gender into Female or Male values...
def replace_str(df):
    for i in df['gender']:
        if i.startswith('f') == True:
            df['gender'] = df['gender'].apply(lambda x: re.sub('^f\w+', 'Female',x))
        elif i.startswith('m') == True:
            df['gender'] = df['gender'].apply(lambda x: re.sub('^m\w+', 'Male',x))
    return df


# Filter at column age with values lenght = 4, and calculate the subtract between 2016 and value
def age(df):
    if len(df) == 4:
        age = np.subtract(2016,int(df))
        return f'{str(age)} years old'
    else:
        return df

# Apply it in dataframe with all rows
def clean_age(df):
    df['age'] = df['age'].apply(age)
    return df

# Get cleaning results concat all functions
def wrangling(df):
    df_lower_case = lower_case(df)
    df_replace_str = replace_str(df_lower_case)
    df_age = age(df_replace_str)
    df_clean_age = clean_age(df_age)
    return df_clean_age