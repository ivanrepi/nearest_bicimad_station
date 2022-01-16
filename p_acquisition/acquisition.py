import pandas as pd
import requests
import sys
sys.path.insert(0,'/Volumes/GoogleDrive/Mi unidad/IRONHACK/bootcamp/projects/data_pipeline_project_m1/p_reporting')
from reporting import create_csv


#In the CSV acquisition moment, drop duplicates. Sep default = ","

def acquisition_csv(path_file,separator=","):
    dataframe = pd.read_csv(path_file,sep=separator).drop_duplicates()
    return dataframe


#We call to the API Instalaciones Madrid, and save the result as a CSV. In case connection fails, we work with CSV saved other times before.

def acquisition_json(path):
    try:
        df=requests.get(path).json()
        df = pd.json_normalize(df['@graph'])
        df.dropna(subset = ["location.latitude","location.longitude"], inplace=True) #Drop the rows where we have not latitude and longitude of the Sports installation
        create_csv(df,"data/raw/instalaciones.csv") #Save the result table in csv
        return df
    except:
        df=pd.read_csv("data/raw/instalaciones.csv", sep=";").drop_duplicates()
        return df
