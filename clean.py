import csv
import matplotlib.pyplot as plt
import numpy as np
arr =[]
with open("Train_data.csv", 'r') as file:
  csvreader = csv.reader(file)
  k = 0
  for row in csvreader:
    if k > 0:
      arr.append(row[0])
    k = k + 1
l = 0
for i in range(len(arr)):
  for k in range(i + 1, len(arr)):
    if(arr[i] == arr[k]):
      print("Duplicate present at: ", arr[i])
      l = 1
if (l == 0):
    print("No duplicates")      # checks for duplicates.NULL values are treated ahead in code
