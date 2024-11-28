#!/usr/bin/env python
# coding: utf-8

# #Importing the raw Storygraph data and previewing it

# In[79]:


import pandas as pd
from datetime import datetime
import glob
import os


#loads the latest raw data file in the books folder
list_of_files = glob.glob('data/raw-data/books/*')
latest_file =max(list_of_files, key=os.path.getctime)
books_data = pd.read_csv(latest_file)

# Preview the data
print(books_data.head())


# #Cleaning up the Data

# In[80]:


# List of relevant columns to keep
columns_to_keep = ['Title', 'Authors', 'Format', 'Read Status', 'Dates Read', 'Star Rating']

# Drop all other columns
books_data = books_data[columns_to_keep]

# Verify the updated dataframe
books_data.head()


# #Handling Missing Data

# In[81]:


print(books_data.isnull().sum())


# In[82]:

#Fills all the columns under Dates Read with the value "Not Read-Not Read"
#This makes it easier when we split the Dates Read column into start date and end date

books_data['Dates Read'] = books_data['Dates Read'].fillna('Not Read-Not Read')
print(books_data.isnull().sum())


# In[83]:


print(books_data)


# #Standardizing Data

# In[84]:


print(books_data['Read Status'].unique())
print(books_data['Format'].unique())


# In[85]:


# Standardize 'Read Status' and 'Format'
books_data['Read Status'] = books_data['Read Status'].str.lower().str.strip()
books_data['Format'] = books_data['Format'].str.lower().str.strip()




# In[86]:


print(books_data)


# In[87]:


problematic_row = books_data[books_data['Dates Read'].str.split('-').apply(len) == 3]
print(problematic_row)


# #Identifying and Cleaning Inconsistent Dates Read

# In[88]:


books_data['Dates Read'] = books_data['Dates Read'].str.split(',', n=1).str[0]


# In[89]:


books_data[['Date Started', 'Date Finished']] = books_data['Dates Read'].str.split('-', expand=True)


# In[90]:


books_data['Date Started'] = pd.to_datetime(books_data['Date Started'], errors='coerce')
books_data['Date Finished'] = pd.to_datetime(books_data['Date Finished'], errors='coerce')


# In[91]:


print(books_data)


# In[92]:


# Dropping Dates Read Column
books_data = books_data.drop(columns=['Dates Read'])


# In[93]:


# Save the cleaned dataframe to a CSV file
currentDateTime = datetime.now().strftime("%m-%d-%Y %H-%M-%S %p")



books_data.to_csv(f'data/cleaned-data/books/cleaned_books_data {currentDateTime}.csv', index=False)


# In[ ]:




