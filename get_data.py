#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# *** Using Quandl to get historical stock prices data (Alternative to Yahoo Finance) ***

"""
1 - get the table for daily stock prices
2 - filter the table for selected tickers, columns within a time range
3 - set paginate to True because Quandl limits tables API to 10,000 rows per call

NOTE:
qopts.columns
Request data from specific columns by passing the qopts.columns parameter. 
If you want to query for multiple columns, include the column names separated by a comma.
    
FILTERS:
.gte=
Modifies the parameter to return values greater than or equal to the requested value
.lte=
Modifies the parameter to return values less than or equal to the requested value
""" 

# Importing Libraries
import quandl
import pandas as pd
import csv
import time

# save retrieved data as a csv file format named stock_price.csv
filename = 'stock_data.csv'

# Function to do authentication & retrieve data from Quandl Wiki table
def get_contents (key):
    quandl.ApiConfig.api_key = key
    try:
        start = pd.to_datetime('2008-03-27')
        end = pd.to_datetime('2018-03-27')
        start_time = time.time()
        
        df = quandl.get_table('WIKI/PRICES', ticker = ['K', 'XOM'], 
                          qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                          date = { 'gte': start, 'lte': end }) 
        
        # Totally optional to check if the retrieved data is exactly what and how you need.
        #print (df)
        
        # "XOM" stock should be at the beggining
        #df_head = df.head()
        #print(df_head)
        
        # "K"stock should be at the bottom
        #df_tail = df.tail()
        #print(df_tail)
        
        # create a new dataframe with 'date' column as index
        new_df = df.set_index('date')
        
        # use pandas pivot function to sort adj_close values by tickers
        sort_df = new_df.pivot(columns='ticker', values='adj_close')
        
        # save data in a csv format file for further analysis
        sort_df.to_csv(filename, sep=',', encoding='utf-8')
        
        # Good to know how long my code took to run =) 
        print("This code took:",time.time() - start_time,"seconds to run! =)")
        
        return True
    except :
        return False
         
try:
    # For convenience your API Key could be stored in the api_key.py file
    print("Looking for api_key.py")
    import api_key
    get_contents(api_key.key)
    
except:
    print("api_key.py not found")
    while True:
        try:
            
            key = str(input("Please paste your API key here: "))
            
            if get_contents(key) : 
                print("Saving file " +  filename + "...")
            else:
                print("Error saving data to " + filename)
            break
        except ValueError:
            print('You must enter your own API key. Learn more by clicking at: https://help.quandl.com/article/320-where-can-i-find-my-api-key')
            










