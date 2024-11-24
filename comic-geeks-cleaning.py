#!/usr/bin/env python
# coding: utf-8

# #Importing the raw Comic Geeks data and previewing it

# In[79]:


import pandas as pd
from datetime import datetime
import glob
import os


#loads the latest raw data file in the comics folder
list_of_files = glob.glob('data/raw-data/comics/*')
latest_file =max(list_of_files, key=os.path.getctime)
comics_data = pd.read_excel(latest_file)

# Preview the data
print(comics_data.head())


# #Cleaning up the Data

# In[80]:


# List of relevant columns to keep
columns_to_keep = ['Publisher Name', 'Series Name', 'Full Title', 'Release Date', 'My Rating']

# Drop all other columns
comics_data = comics_data[columns_to_keep]

#converting release date to datetime


comics_data['Release Date'] = pd.to_datetime(comics_data['Release Date'], errors='coerce')


# In[91]:


print(comics_data)


# Save the cleaned dataframe to a CSV file
currentDateTime = datetime.now().strftime("%m-%d-%Y %H-%M-%S %p")



comics_data.to_csv(f'data/cleaned-data/comics/cleaned_comics_data {currentDateTime}.csv', index=False)


# In[ ]:




