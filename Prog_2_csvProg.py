# -*- coding: utf-8 -*-
"""
Generating a identifying missing parameters in the csv file

Author: Kriyative Edge

"""
#NOTE: Refer the below website for any type of real time datasets for understanding data, parsing data and understand real-time standards of 
# analytics and machine learning
"""
https://archive.ics.uci.edu/ml/datasets.html
"""

#For our understanding, let us consider a simple dataset in .csv format for datapreprocessing and parsing the data in the .csv file 

########################################################
# Working with missing data [identifying missing data and replace those with NaN]
# The dataset we are using in this program is as follows
"""
The Pima Indians Diabetes Dataset involves predicting the onset of diabetes within 5 years in Pima Indians given medical details.

It is a binary (2-class) classification problem. The number of observations for each class is not balanced. There are 768 observations with 8 input variables and 1 output variable. The variable names are as follows:

0. Number of times pregnant.
1. Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
2. Diastolic blood pressure (mm Hg).
3. Triceps skinfold thickness (mm).
4. 2-Hour serum insulin (mu U/ml).
5. Body mass index (weight in kg/(height in m)^2).
6. Diabetes pedigree function.
7. Age (years).
8. Class variable (0 or 1).
The baseline performance of predicting the most prevalent class is a classification accuracy of approximately 65%. Top results achieve a classification accuracy of approximately 77%.
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# mark zero values as missing or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, np.NaN)

print(dataset)

# or to print the first 20 rows of data
#print(dataset.head(20))

# drop rows with missing values
dataset.dropna(inplace=True)
# summarize the number of rows and columns in the dataset by neglecting NaN data
print(dataset.shape)

























