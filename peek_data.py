#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
Ideally, one should first check the raw data, in order to gain insights that you cannot 
get otherwise and see if you need to perform any data manipulation.
'''

# Import Libraries
import pandas as pd 

# View first 10 rows
df = pd.read_csv('stock_price.csv')
peek = df.head(10)
print(peek)

# Check the dimensions of your data
'''
It is good to know how much data you have:
(i) too many rows and the algorithms can take too long to train & too few maybe there is not enough data to train the algorithm 
(ii) too many features and the algorithm can suffer from the curse of dimensionality
'''
shape = df.shape
print(shape)
# 2518 rows, 3 columns

# Data type for each attribute
'''
Categorical (strings, e.g. male/female) or Ordinal (strings, e.g. very happy, happy, ok) features may need to be converted to float or int values
'''
types = df.dtypes
print(types)
# date object, K and XOM float64

# Check for NULL values 
'''
It is important to check if there are Null values in the dataset and how many, as these can
greatly affect an algorithm's robustness.
'''
null_values = df.isnull().sum()
print(null_values)
# No null values. Yayyy!

