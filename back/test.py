# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:59:58 2021

@author: amir
"""
import os , glob
import pickle
import numpy as np
import sys
import pandas as pd




print(os.getcwd())

files=glob.glob('*.pkl')

print(files)

filename = os.getcwd()+"\\"+files[0]

print(filename)

data = [0, 0.25, 0]
data= np.array(data)

data = data.reshape(1, 3)

print(data)

try:
    pickle_model = pd.read_pickle(filename)
except IOError as e:
    print(e)


    
predict = pickle_model.predict(data)

print ('hello',predict)



