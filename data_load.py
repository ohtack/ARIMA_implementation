import pandas as pd
import csv

file = "/Users/hyungtaegoh/Desktop/PythonWorkspace/Project/ARIMA_implementation/TESLA.csv"
data = pd.read_csv(file)
data.head()