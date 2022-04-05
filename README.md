## ASSIGNMENT 4 DATA1202 Repository
In this file, there is a description of python codes which shows the calculation of 100 rows of channel type distribution from the given dataset which contains nearly 4000 rows. Each steps are given and exaplained. From this, anyone can have overall idea about the calculation of channel type distribution.

## Installing libraries
Here, we will use jupyter notebook from Anaconda software. First, we need to install necessary libraries including numpy and pandas to get desired output. Following are libraries we installed in jupyter notebook.
```
#Import Python Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sqlalchemy import create_engine
```

## Explanation
We are going to perform these codes in order to get 1000 rows output. First of all, we created a function with the parameters and then we loaded the data from first row to last with givenn codes in the python file. Then, we count the value as df1. Then, we loaded the top 1000 rows from the dataset using the a python function which is given in the python file. 
We also loaded the data to a database table. So, we needed a connection to database and for that, we created an engine. As a result, we were able to load the data to a database table.

## Author
Mohammedmusael Shaikh

## Acknowledgement 
The code which we used in python file have been taken from Assignment #4 of DATA1202.

https://github.com/MS22-Git/Data1202Assignment.git
