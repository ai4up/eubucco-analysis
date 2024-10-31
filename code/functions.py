
import os
import re
import pandas as pd
from variables import countries_eubucco


def check_and_read_markdown(file_path, subsection_title):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return f"The file '{file_path}' does not exist."

    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()

    # Use a regular expression to find the specific subsection
    pattern = re.compile(rf"## {re.escape(subsection_title)}(.*?)(##|$)", re.DOTALL)
    match = pattern.search(content)

    # If the subsection is found, return its content
    if match:
        subsection_content = match.group(1).strip()
        return subsection_content
    else:
        return f"Subsection '{subsection_title}' not found in the file."

def load_v01_vs_msft():
    df_all = pd.DataFrame()

    for country in countries_eubucco:
        df_msft = pd.read_csv(f'../data/overview-msft/{country}_overview.csv')
        df_eubucco = pd.read_csv(f'../data/overview-v0_1/{country}_overview.csv')
        df_eubucco['id'] = [s.split('-')[1] for s in df_eubucco.id]
        df_msft['id'] = [s.split('-')[1] for s in df_msft.id]
        df = pd.merge(df_msft,df_eubucco,on="id",suffixes=("_msft","_v01"))
        df_all = pd.concat([df_all,df],axis=0)
    
    return(df_all)