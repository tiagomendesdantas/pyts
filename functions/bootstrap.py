#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math as mt



def mbb(serie,window_size):
    """
    This function performs Moving Block Bootstrap.
    It is ideal if you want to perform Bootstrap on time series
    
    """
    bx = np.zeros(mt.floor((len(serie)/window_size)+2)*window_size)
    for i in range(mt.floor(len(serie)/window_size)+2):
        c=int(np.random.choice(len(serie)-window_size+1,1))
        bx[i*window_size:((i+1)*window_size)]=serie[c:(c+window_size)]
    start_from = int(np.random.choice(window_size))
    bx[start_from:(start_from+len(serie))]
    return bx

