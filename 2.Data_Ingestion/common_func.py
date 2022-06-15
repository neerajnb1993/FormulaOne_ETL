#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()
from pyspark.sql.functions import current_timestamp


# In[2]:


def add_timestamp(input_df):
    input_df = input_df.withColumn('ingestion_Date',current_timestamp())
    
    return input_df


# In[ ]:




