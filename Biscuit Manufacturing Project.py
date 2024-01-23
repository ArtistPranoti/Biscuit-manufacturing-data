#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_excel(r"C:\OEE Manufacturing Data.xlsx")
print(data)


# In[4]:


data.info()


# In[5]:


data.head()


# In[6]:


#null values
null_values = data.isnull().sum()


# In[8]:


null_values_column = data['Duration'].isnull().sum()


# In[9]:


print("Null values in the entire DataFrame:")
print(null_values)

print("\nNull values in a specific column:")
print(null_values_column)


# In[12]:


# Assuming 'df' is your DataFrame
# Check for duplicate rows in the entire DataFrame
duplicate_rows = data[data.duplicated()]


# In[15]:


duplicate_rows_columns = data[data.duplicated(subset=['Product'])]


# In[16]:


print("Duplicate rows in the entire DataFrame:")
print(duplicate_rows)

print("\nDuplicate rows based on specific columns:")
print(duplicate_rows_columns)


# In[ ]:




