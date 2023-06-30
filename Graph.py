import csv
import matplotlib.pyplot as plt
import numpy as np
arr =[]  #example of graph
with open("Train_data.csv", 'r') as file:
  csvreader = csv.reader(file)
  k = 0
  for row in csvreader:
    if k > 0:
      arr.append(row[3])
    k = k + 1
bachelor = 0
master = 0
none = 0
other = 0
for i in range(len(arr)):
  if(arr[i] == "Bachelor's"):
    bachelor = bachelor + 1
  elif(arr[i] == "Master's & above"):
    master = master + 1
  elif(arr[i] == ""):
    none = none + 1
  else:
    other = other + 1
print(other)
plt.xlabel("Education Level")
plt.ylabel("No of Employees")
plt.title("Education data")
plt.bar(["Below Secondary","Bachelor's", "Master's", "No Degree"], [other,bachelor,master,none])
plt.show()
