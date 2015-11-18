#Jhanelle Williams 18-11-2015
# coding: utf-8

# ###Codes for Final Project
# Understanding Water Quality in the Main Arm of the Fraser River

# In[301]:

# import libraries

import pandas as pd
import matplotlib.pyplot as plt

#import stats library

import statsmodels.api as sm
import scipy

#The function below is used to show the plots within the notebook

get_ipython().magic('matplotlib inline')


# In[91]:

#Check version of pandas library
pd.__version__


# In[93]:

#Path from which the data is retrieved
filepath= '../data/Fraser_River_Water_Data.csv'

def load_water_quality_data():
    '''This function loads the dataset required to complete this project.'''
    
    #Function used load data
    water_quality_data= pd.read_csv(filepath, delimiter= ',')
    
    return(water_quality_data)


# In[94]:

#Print the head of the data set
load_water_quality_data().head()


# In[95]:

#Import pasty library to run data

from patsy import dmatrices
from patsy.builtins import *


# In[129]:


def extract_and_drop_data():
    
    '''This function extracts the variables needed, drop the NaN values and rename these columns such 
    as to eliminate patsy error'''
    
    #Extract variables to be analyzed for assignment
    fraser_water_quality_testing=load_water_quality_data()[['Sample time', 'Temperature Water [Lab: 80] [VMV: 1125]',
                                                          'Oxygen Dissolved [Lab: -54] [VMV: 1124]']]
    
    #Remove the NaN from the dataset
    water_quality_DO=fraser_water_quality_testing.dropna()
    
    #Change column names to eliminate the possibility of patsy error when doing linear regression
    water_quality_DO2= water_quality_DO.rename(columns={'Sample time': 'Sample_time','Temperature Water [Lab: 80] [VMV: 1125]':'Temperature_Lab80',
                                                    'Oxygen Dissolved [Lab: -54] [VMV: 1124]':'Oxygen_Dissolved_Lab-54'})
    return water_quality_DO2


# In[132]:

#Use the defined function to rename column names and drop empty values

edited_columns=extract_and_drop_data()


# In[137]:

#Print a new dataframe with the munged data
edited_columns


# In[283]:

def linear_model(x,y):
    '''This function is used to create a linear regression for x and y variables in the dataset.
    The input for the function are the x and y variables while the output is a 
    linear model that represents these variables'''
    
    #Define the x and y variables
    y= 'Oxygen_Dissolved_Lab-54'
    x= 'Temperature_Lab80'
    
    #General form for the linear model formula, this would be used with the defined variable
    lm= sm.formula.ols(formula= "Q('" + y + "') ~ Q('" + x + "')", data= edited_columns).fit()
    
    # Used to predict function we make a data frame, therefore below we have data frame that is used to make dataframe
    x_new=pd.DataFrame({'Temperature_Lab80': range(1,700)})
    
    # create a predict function to calculate linear model
    y_preds=lm.predict(x_new)
    
    return lm
    return x_new
    return y_preds
    


# In[271]:

#Create a variable for the parameters of the linear model 
parameters_linear_model=linear_model('Temperature_Lab80','Oxygen_Dissolved_Lab-54').params


# In[272]:

#Print the parameters of the linear model
parameters_linear_model


# In[273]:

#Create a summary for linear model 
summary_of_linear_model=linear_model('Temperature_Lab80','Oxygen_Dissolved_Lab-54').summary()


# In[260]:

#Print the summary of the linear model values
summary_of_linear_model


# In[300]:

#Create the dimensions of the figure size for the plot created
plt.figure(figsize=(20,20))

#Plot the linear model for the dataset
plot_water_quality= edited_columns.plot(kind='scatter', x='Temperature_Lab80', y="Oxygen_Dissolved_Lab-54")

#Create the x limits for the graph
plt.xlim(0,25)

#Create the y limits for the graph
plt.ylim(0,18)

#Define the y_preds variable
y_preds=linear_model('Temperature_Lab80','Oxygen_Dissolved_Lab-54').predict(x_new)

#Create a plot that displays the linear model
plt.plot(x_new, y_preds, c='blue', linewidth=3)

#Set title for the linear regression model
plt.title('The relationship between Dissolved Oxygen and Temperature in the Fraser River Main Arm', fontsize=9)

#Save the linear model plot
plt.savefig('../results/Fraser_River_Water_Quality_Graph_01.pdf')

plt.show()


# In[ ]:




# In[ ]:



