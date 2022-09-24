import pandas as pd
import numpy as np

def preprocess(b_report):
    # load the dataset
    b_report = pd.read_csv('breach_report.csv', encoding='latin5')
    
    # Let's replace the empty strings with NaN values
    b_report = b_report.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    b_report = b_report.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    b_report = b_report.replace('.', np.nan)
    
    # Let's replace \N(always add an extra forward class) (\\N) with NaN values
    b_report = b_report.replace('\\N', np.nan)
    
    # check for duplicate rows in the dataset -> 
    b_report.duplicated().sum()
    
    # drop duplicated rows
    b_report.drop_duplicates(inplace=True)
    
    # if a row has all NA values drop the row
    b_report.dropna(axis=0, how='all', inplace=True)
    
    b_report['Location of Breached Information'].fillna(b_report['Location of Breached Information'].mode()[0], inplace=True)
    b_report['State'].fillna(b_report['State'].mode()[0], inplace=True)
    b_report['Type of Breach'].fillna(b_report['Type of Breach'].mode()[0], inplace=True)
    b_report['Covered Entity Type'].fillna(b_report['Covered Entity Type'].mode()[0], inplace=True)
    b_report['Web Description'].fillna(b_report['Web Description'].mode()[0], inplace=True)
    b_report['Individuals Affected'].fillna((b_report['Individuals Affected'].mean()), inplace=True)
    
    return b_report