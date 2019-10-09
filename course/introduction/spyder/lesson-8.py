#!/usr/bin/env python
# coding: utf-8

#%%
# # Using DataFrames
# 
# This lesson introduces:
# 
# * Computing returns (percentage change)
# * Basic mathematical operations on DataFrames
# * Common DataFrame methods (functions)
# 
# This first cell load data for use in this lesson.

#%%
# Setup: Load prices
import pandas as pd
prices = pd.read_hdf("data/dataframes.h5", "prices")
sep_04 = pd.read_hdf("data/dataframes.h5", "sep_04")
goog = pd.read_hdf("data/dataframes.h5", "goog")


#%%
# ## Problem: Compute Returns
# 
# Compute returns using 
# 
# ```python
# returns = prices.pct_change()
# ```
# 
# which computes the percentage change.
# 
# Additionally, extract returns for each name using 
# 
# ```python
# spy_returns = returns["SPY"]
# ```

#%%


#%%


#%%


#%%
# ## Problem: Compute Log Returns
# 
# ```python
# import numpy as np
# 
# log_returns = np.log(prices).diff()
# ```
# 
# first difference of the natural log of the prices. Mathematically this is 
# $r_{t}=\ln\left(P_{t}\right)-\ln\left(P_{t-1}\right)=\ln\left(\frac{P_{t}}{P_{t-1}}\right)\approx\frac{P_{t}}{P_{t-1}}-1$.

#%%


#%%
# ## Problem: Basic Mathematical Operations
# 
# |  Operation            | Symbol | Precedence |
# |:----------------------|:------:|:----------:|
# | Parentheses           | ()     | 4          |
# | Exponentiation        | **     | 3          |
# | Multiplication        | *      | 2          | 
# | Division              | /      | 2          |
# | Floor division        | //     | 2          |
# | Modulus               | %      | 2          | 
# | Matrix multiplication | @      | 2          |
# | Addition              | +      | 1          |
# | Subtraction           | -      | 1          |
# 
# **Note**: Higher precedence operators are evaluated first, and ties are
# evaluated left to right. 
# 
# 1. Add 1 to all returns
# 2. Square the returns
# 3. Multiply the price of Google by 2. 
# 4. Extract the fractional return using floor division and modulus
# 5. Add the returns on SPY to those of AAPL 

#%%


#%%


#%%


#%%


#%%


#%%


#%%
# ## Problem: Non-conformable math
# 
# Add the prices in `sep_04` to the prices of `goog`. What happens? 

#%%


#%%
# ## Problem: Constructing portfolio returns
# Set up a 3-element array of portfolio weights 
# 
# $$w=\left(\frac{1}{3},\,\frac{1}{3}\,,\frac{1}{3}\right)$$
# 
# and compute the return of a portfolio with weight $\frac{1}{3}$ in each security.
# 

#%%


#%%
# Repeat the previous calcuation using multiplication (`*`) and `.sum()`.
# **Note**: You need to use the `axis` keyword for the sum.

#%%


#%%
# ## Problem: Mean, Standard Deviation and Correlation
# 
# Using the function mean, compute the mean of the three returns series one at a time. For example  
# ```python
# goog_mean = goog_returns.mean()
# ```
# Next, compute the mean of the matrix of returns using  
# 
# ```python
# retmean = returns.mean()
# ```
# 
# What is the relationship between these two? Repeat this exercise for the standard deviation (`std()`).
# Finally, compute the correlation of the matrix of returns (`corr()`). 

#%%


#%%


#%%


#%%


#%%
# ## Problem: Summing all elements
# 
# Compute the sum of the columns of returns using `.sum()`. How is this related to the mean computed 
# in the previous step? 

#%%


#%%


#%%
# ## Problem: Maximum and Minimum Values
# Compute the minimum and maximum values of the columns of returns using the `min()` and `max()` commands. 

#%%


#%%


#%%
# ## Problem: Rounding Up, Down and to the Closest Integer
# 
# Rounding up is handled by ceil, rounding down is handled by floor and rounding to the closest 
# integer is handled by round. Try all of these commands on 100 times returns. For example,  
# ```python
# rounded = (100*returns).round()
# ``` 
# 
# Use `ceil` and `floor` to round up and down, respectively.

#%%


#%%


#%%
