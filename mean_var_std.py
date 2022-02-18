#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[17]:


def calculate(matrix):
    array = np.array(matrix).reshape(3,3)
    print('mean:',np.mean(array, axis = 0),np.mean(array, axis = 1),np.mean(array))
    print('variance:',np.var(array, axis = 0),np.var(array, axis = 1),np.var(array))
    print('standard deviation:',np.std(array, axis = 0),np.std(array, axis = 1),np.std(array))
    print('max:',np.amax(array, axis = 0),np.amax(array, axis = 1),np.amax(array))
    print('min:',np.amin(array, axis = 0),np.amin(array, axis = 1),np.amin(array))
    print('sum:',np.sum(array, axis = 0),np.sum(array, axis = 1),np.sum(array))


# In[18]:


l1 = [0,1,2,3,4,5,6,7,8]    
calculate(l1)


# In[ ]:




