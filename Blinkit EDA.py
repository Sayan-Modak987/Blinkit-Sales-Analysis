#!/usr/bin/env python
# coding: utf-8

# ## **Data Analysis Python Project - Blinkit Analysis**
# 

# **Import Libraries**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **Importing Raw Data**

# In[4]:


df=pd.read_excel('BlinkIT Grocery Data.xlsx')
df.head(10)


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.dtypes


# ### **Business Requirements**

# ### **KPI's**

# In[16]:


#Total Sales
total_sales =df['Sales'].sum()

#Average Sales
average_sales =df['Sales'].mean()

#No. of Items Sold
no_of_items_sold=df['Sales'].count()

#Average Ratings
average_ratings = df['Rating'].mean()

#Display

print(f"Total_Sales: ${total_sales:,.0f}")
print(f"Average_Sales: ${average_sales:,.0f}")
print(f"No of Items Sold: {no_of_items_sold:,.0f}")
print(f"Average Ratings: {average_ratings:,.0f}")


# ### **Charts Requirement**

# ### **Total Sales by Fat Content**

# In[19]:


sales_by_fat=df.groupby('Item Fat Content')['Sales'].sum()
plt.pie(sales_by_fat, labels=sales_by_fat.index,autopct='%.1f%%',startangle=90)
plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show;


# ### **Total sales by item type**

# In[23]:


sales_by_type =df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars =plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation=90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height(),
            f'{bar.get_height():,.0f}', ha='center',va='bottom',fontsize=8)
    
plt.tight_layout()
plt.show();


# ### **Fat Content by Outlet for Total Sales**

# In[25]:


grouped = df.groupby(['Outlet Location Type','Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular','Low Fat']]

ax=grouped.plot(kind='bar',figsize=(8,5),title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show();


# ### **Total Sales by Outlet Establishment**

# In[27]:


sales_by_year=df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()
plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index,sales_by_year.values,marker='o',linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index,sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}',ha='center',va='bottom',fontsize=8)
    
plt.tight_layout()
plt.show();


# ### **Total Sales by Outlet Size** 

# In[29]:


sales_by_size=df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size,labels=sales_by_size.index, autopct='%1.1f%%' ,startangle=90)
plt.title('Outlet size')
plt.tight_layout()
plt.show();


# ### **Total Sales by Location**

# In[34]:


sales_by_location=df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales',ascending=False)

plt.figure(figsize=(8,3))
ax=sns.barplot(x='Sales',y='Outlet Location Type',data=sales_by_location)

plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')

plt.tight_layout()
plt.show()


# In[ ]:




