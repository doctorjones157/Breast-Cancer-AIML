#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
import pandas as pd 
#Q1
print(np.arange(0,18).reshape(6,3))

df1 = pd.read_excel(r"D:\Users\rannamalai\Downloads\Week 1 Dataset.xlsx")
df2 = df1.rename(columns={'Name':'First Name','Income per month':'Income monthwise','State':'States(India)','Age':'Lifetime','Sex':'Gender','Number of siblings':'Siblings'},errors="raise")
#Q2
print(df2)
df2.rename(columns={'Income monthwise':'Income/month','Lifetime':'Duration of Life'},inplace="true")
#Q3
print(df2)
#Q4
print(df1[['Sex','Number of siblings']])
#Q5
print(df1.iloc[2:10,0:5])
#Q6
sumOfSib = df1['Number of siblings'].sum()
print("---------------------------------------")
print(sumOfSib)
#Q7
#Independent variables are Income per month and age, sibilings in the dependent variable because it change when income per month change
#Q8
#I have tried find the findings in heatmap, but I can't understand the heatmap


# In[ ]:




