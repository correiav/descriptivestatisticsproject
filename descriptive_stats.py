#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''To understand data distribution completely and properly we measures such as: 
1 - measures of central tendency (mean, median, mode)
2 - measures of dispersion (standard deviation, variance)
3 - measures to describe shape of a distribution 

Such measures are part of the descriptive statistics scope, which allows to summarize data
in order to get further insights and help with the decision of what comes next: inferential stats or complex algorithms...
'''

# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading csv file
df = pd.read_csv('stock_price.csv')

# K Stock Descriptive Stats
kelloggs = df['K']

mean = kelloggs.mean()
median = kelloggs.median()
mode = kelloggs.mode()
print('\n')
print('Descriptive Statistics for Kellogs Stock \n')
print('Mean: ',mean,'\nMedian: ',median,'\nMode: ',mode[0])

plt.figure(figsize=(10,5))
plt.hist(kelloggs,bins=10,color='grey')
plt.axvline(mean,color='red',label='Mean')
plt.axvline(median,color='yellow',label='Median')
plt.axvline(mode[0],color='green',label='Mode')
plt.title('Frequency Distribution of Closing Stock Price for Kellogs')
plt.xlabel('Kellogs - Stock Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# XOM Stock Descriptive Stats
exxon = df['XOM']

mean = exxon.mean()
median = exxon.median()
mode = exxon.mode()
print('\n')
print('Descriptive Statistics for Exxon Mobil Stock \n')
print('Mean: ',mean,'\nMedian: ',median,'\nMode: ',mode[0])

plt.figure(figsize=(10,5))
plt.hist(kelloggs,bins=10,color='grey')
plt.axvline(mean,color='red',label='Mean')
plt.axvline(median,color='yellow',label='Median')
plt.axvline(mode[0],color='green',label='Mode')
plt.title('Frequency Distribution of Closing Stock Price for Exxon Mobil')
plt.xlabel('Exxon Mobil - Stock Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# The 'describe' method generates descriptive stats that summarize measures of central tendency, dispersion and shape of data
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
summary = df.describe()
print('\n')
print('Descriptive Stats summary for K & XOM Stocks \n \n'+ str(summary))  

'''              K       XOM
count  2518.000  2518.000 
mean     52.809    71.473 
std      12.862    11.723 
min      27.741    45.231
25%      41.938    61.082
50%      53.135    74.555
75%      62.901    80.740
max      83.924    92.545

The descriptive summary above suggests:

Given the average, XOM stock has performed 35% better over time than the K stock.
The stock prices did not have a high volatility in performance, as per comparison of std values.
25%(Lower Quartile) of the stock prices have values <= 41.938 - K & 61.082 - XOM
50% (Median) of the stock prices have values <= 53.135 - K & 74.555 - XOM
75% (Upper Quartile) of the stock prices have values <= 62.901 - K & 80.740 - XOM
 
'''
# Calculate the percentage increase given mean values for K & XOM
#xom = float(71.473)
#k = float(52.809)
#percentage_change = (xom - k) / k * 100
#print('\n')
#print('Percentage increase over the last 10 years given mean value: ' + str(percentage_change))









    
    

