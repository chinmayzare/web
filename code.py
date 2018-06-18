
# coding: utf-8

# In[2]:


from flask import Flask, render_template, abort, redirect, url_for, escape, request, session, g
import pandas as pd
import os
import holoviews as hv
hv.extension('bokeh', 'matplotlib')
from bokeh.plotting import save
renderer = hv.renderer('bokeh')
get_ipython().magic(u'matplotlib inline')
df = pd.read_csv('realdata.csv')
df.bsfile = df.bsfile.astype(str)
dataset = hv.Dataset(df)


# In[3]:


#Curve function
def Plot(var):
    h = hv.Curve( df, 'sst', var)

    h = h.options(width = 15500, height = 350, line_width = 3, xrotation = 45, tools=['hover'], toolbar= 'left')
    renderer.save(h, 'myproject/' + var)
    return 


# In[4]:


vdims = ['PM2_Conf_Ring_Pos_Mon', 'PM2_DC_Bias_Comp', 'PM2_Gas_01_Flow_Mon', 'PM2_Gas_02_Flow_Mon', 'PM2_Gas_03_Flow_Mon']

for i in range(4):
    c = Plot(vdims[i])


# In[58]:


#df['sst'] = pd.to_datetime.strftime(df.sst)


# In[6]:


df['sst'] = df.sst.astype(str)


# In[7]:


df.head()


# In[8]:


df['sst'] = df.sst.str.slice(6,16,1)


# In[9]:


df['lot_no'].value_counts().sort_index().plot()

