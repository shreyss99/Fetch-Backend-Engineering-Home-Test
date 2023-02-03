import sys
import pandas as pd


def convert_file_to_dataframe(file_name):
    
    input_dataframe = pd.DataFrame()
    try:
        input_dataframe = pd.read_csv(file_name)
    except FileNotFoundError:
        print("The file {0} is not located in the current working directory".format(file_name))
    return input_dataframe