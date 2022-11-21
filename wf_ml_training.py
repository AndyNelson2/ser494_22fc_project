import random

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fileObject = open("data_processed/training_data.txt", "r")
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

numpy_array = np.array(data, dtype=float)
data2 = pd.DataFrame(numpy_array, columns=['x', 'y'])

X = data2['x'].values
Y = data2['y'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

m = len(X)

top = 0
bot = 0
for i in range(m):
    top += (X[i] - mean_x) * (Y[i] - mean_y)
    bot += (X[i] - mean_x) ** 2
b1 = top / bot
b0 = mean_y - (b1 * mean_x)

y_predicted = []
for i in range(len(Y)):
    y_predicted.append(b1 * X[i] + b0)
print("Model: ", b1, 'x', '+', b0)

outfile = open('models/LinearRegression.txt', 'a')
outfile.write(str(b1) + ' ' + str(b0) + '\n')
outfile.close()

plt.scatter(X, Y)
plt.plot(X, y_predicted)
plt.show()