import pandas as pd
import numpy as np

PATH = '../data/autos.csv'

def read_data(PATH):
    '''
    Read data from dataset from path
   
    Parameters
    ----------
    PATH : str
        path source of training data, csv.
    
    Returns
    -------
    data : pd.DataFrame
        Data for modeling
    '''
    data = pd.read_csv(PATH, encoding='cp1252')
    
    return data
