#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as nm


# In[2]:


pwd


# In[10]:


get_ipython().run_line_magic('cd', '\\Users\\ravia\\downloads')


# In[12]:


df= pd.read_excel('BlueJaysThreeMonthScores.xlsx')


# In[14]:


df= pd.read_csv('reddit_vm.csv')


# In[15]:


df


# In[16]:


df.columns


# In[17]:


df.shape


# In[18]:


df.head()


# In[19]:


df.tail(3)


# In[20]:


df.describe()


# In[21]:


df.hist()


# In[22]:


df.boxplot()

