#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math as mt
from statsmodels.tsa.seasonal import STL



def mbb(serie,window_size):
    """
    This function performs Moving Block Bootstrap
    
    """
    bx = np.zeros(mt.floor((len(serie)/window_size)+2)*window_size)
    for i in range(mt.floor(len(serie)/window_size)+2):
        c=int(np.random.choice(len(serie)-window_size+1,1))
        bx[i*window_size:((i+1)*window_size)]=serie[c:(c+window_size)]
    start_from = int(np.random.choice(window_size))
    bx=bx[start_from:(start_from+len(serie))]
    return bx

def stl_mbb(serie,frequency,b):
    """
    This function generates new versions of the time series 
    via Bootstraping the residuals of the STL decomposition
    
    """
    model = STL(serie,frequency).fit()
    residual = model.resid
    trend = model.trend
    seasonal = model.seasonal
    
    versions=np.zeros((len(residual),b))
    
    for i in range(b): 
        versions[:,i]=mbb(residual,2*frequency)+trend+seasonal
    
    return versions
    
    

