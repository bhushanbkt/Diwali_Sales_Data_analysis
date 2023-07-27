#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import Library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


import warnings
warnings.filterwarnings('ignore')


# In[7]:


df= pd.read_csv('Diwali Sales Data.csv',encoding='unicode_escape')
df


# ### Data preprocessing

# In[8]:


df.shape


# In[9]:


df.info()


# In[10]:


# Drop null columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)
df


# In[11]:


df.isna().sum()


# In[12]:


df.dropna(inplace=True)


# In[13]:


df.isna().sum()


# In[15]:


df.info()


# ### Exploratory data analysis (EDA) 

# In[17]:


df.describe()


# In[19]:


df.columns


# In[59]:


plt.figure
sns.countplot(df['Gender'],data=df['Gender']);


# In[46]:


(df['Gender'].value_counts())


# In[55]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen);


# From above graphs we can conclude that the most of the buyers are females than men

# In[ ]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[60]:


sns.countplot(df['Age Group']);


# In[62]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age);


# From above graphs we can conclude that the most of the buyers are in age group of 26-35

# In[65]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders');


# From above graphs we can see that the most of the orders from Uttar Pradesh, Maharashtra and Karnataka respectively

# In[67]:


#Orders and sectors
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount');


# From above graphs we can conclude that orders comes from  buyers are working in IT, Healthcare and Aviation sector

# In[76]:


#Most order Product Category
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount');


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# **Conclusion/Summary**

# ***1.the most of the buyers are females than men***
# 
# ***2.most of the buyers are in age group of 26-35***
# 
# ***3. the most of the orders from Uttar Pradesh, Maharashtra and Karnataka respectively ****
# 
# ***4. orders comes from buyers are working in IT, Healthcare and Aviation sector ****
# 
# ***5.most of the sold products category are from Food, Clothing and Electronics  ****
# 

# In[ ]:




