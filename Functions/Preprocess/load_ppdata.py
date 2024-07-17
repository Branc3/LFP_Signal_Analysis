import numpy as np
import scipy as sp
import pickle

def read_ppdata(dataFile):
    if '.pkl' in dataFile:
        with open(dataFile,'rb') as f:
            loaded_data = pickle.load(f)
    
    if '.mat' in dataFile:
        sp.io.loadmat(dataFile)
    return