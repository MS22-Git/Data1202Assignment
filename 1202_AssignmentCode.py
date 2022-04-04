#Import Python Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sqlalchemy import create_engine

#Read csv file
df = pd.read_csv("youtube_dataset.csv",encoding = "ISO-8859-1")

#Find how many records this data frame has
df.head()

Create function
def channeltype_distribution(firstrow,lastrow):
    
    #Load top records of the original 4000 records
    df1=df.iloc[firstrow:lastrow]

    #Count the number of unique values in our data
    df2=df1.channeltype.value_counts(dropna=True)
    
    #Plotting into a graph
    df3=df2.plot(kind='bar',xlabel='Channel Types',ylabel='Frequency',title='Distribution of Channel Types')

    return df2
  
  #calling the function
channeltype_distribution(0,1000)

#Load top 1000 records of the original 4000 into a separate CSV file
df1=df.iloc[0:1000]
df1.to_csv('output1000.csv',index=False)

# create engine
engine = create_engine('mysql+pymysql://root:krish123@localhost/data1202')

# connection string
conn = engine.connect()

#Load only the top 1000 records of the original 4000 into a database table
df1.to_sql('youtube_details', con=engine, if_exists='replace',index_label='id')

# read a simple query into DataFrame
df5 = pd.read_sql("SELECT * FROM data1202.youtube_details", conn)
df5

