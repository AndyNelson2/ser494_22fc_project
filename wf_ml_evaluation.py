import random

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

fileObject = open("data_original/data.txt", "r")
data = []
parsed_data = []
while True:
    line = fileObject.readline()
    if not line:
        break
    data.append(line)

# gets just the numbers from data.txt
for line in data:
    data_points = []
    thirdString = line[0:line.find('4th &')]
    fourthString = line[line.find('4th &'):len(line)]

    rd = thirdString.find('3rd &')
    th = fourthString.find('4th &')

    # first appends how many yards the team needed on third down
    if thirdString[rd + 6: rd + 8] == 'Go':
        rd = thirdString.find('3rd & Goal at')
        data_points.append(thirdString[rd + 17: rd + 19].strip())
    else:
        data_points.append(thirdString[rd + 6: rd + 8].strip())

    # then appends how many yards they gained (will always be less)
    if not thirdString.__contains__("yard"):
        data_points.append(0)
    else:
        strn = thirdString[thirdString.find('yard') - 3:thirdString.find('yard') - 1].strip()
        if strn.__contains__('\''):
            strn = strn[0:len(str)]
        data_points.append(strn)

    # then appends how many yards the team needed on fourth down
    if fourthString[th + 6: th + 8] == 'Go':
        th = fourthString.find('4th & Goal at')
        data_points.append(fourthString[th + 17: th + 19].strip())
    else:
        data_points.append(fourthString[th + 6: th + 8].strip())

    # then adds how many yards they gained
    if not fourthString.__contains__("yard"):
        data_points.append(0)
    else:
        data_points.append(fourthString[fourthString.find('yard') - 3:fourthString.find('yard') - 1].strip())

    # finally, adds if it was a successful attempt or not

    if int(data_points[2]) < int(data_points[3]):
        data_points.append(True)
    else:
        data_points.append(False)

    parsed_data.append(data_points)

# makes 3 arrays that will hold data for if a set of downs was a success or failure
# arrays have 100 indexes with each index representing the percentage of needed yards gained on third down
# for example: if it's 3rd & 8 and the team gets 2 yards and then the team fails on 4th down then in the
# 'failures' array the 25th index (2/8) will be incremented by 1
successes = []
failures = []
overall = []
for x in range(101):
    successes.append(0)
    failures.append(0)
for point in parsed_data:
    num1 = int(point[1])
    if point[0].__contains__("'"):
        num2 = int(point[0][0:len(point[0]) - 1])
    else:
        num2 = int(point[0])
    ratio = num1 / num2
    rounded = round(ratio * 100)

    if rounded >= 100:
        rounded = 100
    if rounded < 0:
        rounded = 0
    if point[4]:
        successes[rounded] += 1
    else:
        failures[rounded] += 1
    # print(point, ratio, rounded)

# combines failure and success arrays into overall array which holds the percentage of times the team had a successful
# set of downs based on the percentage of needed yards they got on 3rd down
# for example: if there were 5 drives where a team got 20% of their yards on third down and 3 drives resulted in a
# first down and 2 didn't then the 20th index of 'overall' will be 0.6
for x in range(101):
    if successes[x] != 0 or failures[x] != 0:
        overall.append([x, successes[x] / (successes[x] + failures[x])])

print(overall)
random.shuffle(overall)
data_training = overall[0:round((len(overall) * 0.8))]
data_testing = overall[round((len(overall) * 0.8)):len(overall)]
#print(data_training)
#print(data_testing)

outfile = open('data_processed/training_data.txt', 'w')
for pair in data_training:
    outfile.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
outfile.close()

outfile = open('data_processed/testing_data.txt', 'w')
for pair in data_testing:
    outfile.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
outfile.close()



'''
numpy_array = np.array(data_training, dtype=float)
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
plt.scatter(X, Y)
plt.plot(X, y_predicted)
plt.show()
'''
