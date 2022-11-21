import random

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fileObject = open("data_processed/testing_data.txt", "r")
data = []
temp_data = []
while True:
    line = fileObject.readline()
    if not line:
        break
    broken_line = line.split(" ")
    temp_data = [broken_line[0], broken_line[1]]
    data.append(temp_data)
fileObject.close()

modelFile = open('models/LinearRegression.txt', 'r')
line = modelFile.readline()
broken_line = line.split(" ")

b1 = float(broken_line[0])
b0 = float(broken_line[1])

numpy_array = np.array(data, dtype=float)
data2 = pd.DataFrame(numpy_array, columns=['x', 'y'])

X = data2['x'].values
Y = data2['y'].values

y_predicted = []
for i in range(len(X)):
    y_predicted.append(b1 * X[i] + b0)

plt.scatter(X,Y)
plt.plot(X,y_predicted)
plt.show()

MSE = 0.0
count = 0
for number in y_predicted:
    MSE += ((number - Y[count]) * (number - Y[count]))
    count += 1
MSE *= (1/len(y_predicted))
print("MSE:", MSE)