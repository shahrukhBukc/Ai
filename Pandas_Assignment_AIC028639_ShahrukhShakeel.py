#!/usr/bin/env python
# coding: utf-8

# # Pandas Assignment.
# 

# ### 1. Create a data series with marks of students : 75, 80, 79, 60

# In[16]:


import pandas as pd
import os
marks =pd.Series([75,80,79,60])
print(marks)


# ### 2. Create a data frame with name of students, id and marks

# In[26]:


student=pd.DataFrame({'Name':['Shahrukh','Jawad','Yaseen','Faraz'],'Id':[1,2,3,4],'Marks':marks})
display(student)


# ### 3. Now read the file 'data.csv' in panda

# In[28]:


uni_df=pd.read_csv('data.csv')
uni_df


# ### 4. What are the columns in the dataframe?

# In[33]:


uni_df.columns


# ### 5. Sort the data based on Marks obtained. Fill all the 'na' cells with 0

# In[36]:


sorted_data=uni_df.sort_values('Total (100)',ascending=False).fillna(0)
sorted_data


# ### 6. Display the top 10 rows

# In[38]:


sorted_data.head(10)


# ### 7. Display the last 10 rows

# In[39]:


sorted_data.tail(10)


# ### 8. Display only the odd rows

# In[40]:


sorted_data[1::2]


# ### 9. Display only those students who got failed in examination

# In[44]:


sorted_data[sorted_data['Grade'].str.contains('F')]


# ### 10. Find out the basic statistical info about data

# In[60]:


sorted_data.describe()


# ### 11. How many students got A, B, C, F?

# In[64]:


sorted_data['Grade'].value_counts().sort_index()


# ### 12. What are the mean scores for students who got A, B, C, F?

# In[66]:


sorted_data.groupby('Grade').mean()


# In[ ]:




