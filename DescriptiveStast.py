# Packages Loading
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Loading
Chicago = pd.read_csv('chicago.csv')
new_york_city= pd.read_csv('new_york_city.csv')
washington= pd.read_csv('washington.csv')

##
### Descriptive Stastices
##"""Descriptive Stastices For Chicogo Data Sets"""
print("---------Descriptive Stastices head() For Chicogo Data Sets----------\n")
print("Head For Chicago Data set",Chicago.tail(),Chicago.describe(),Chicago.head())
print("---------Descriptive Stastices For New_york_City Data Sets----------")
print("Head,Tail,Describe For New_york_City_DS Data set",new_york_city.head(),new_york_city.tail(),new_york_city.describe())
print("---------Descriptive Stastices For Washington Data Sets----------")
print("Head,tail,Describe For washington Data set",washington.head(),washington.tail(),washington.describe())


x = Chicago['User Type'].count()
y = Chicago['Gender'].count()

plt.scatter(x,y)
plt.show()

