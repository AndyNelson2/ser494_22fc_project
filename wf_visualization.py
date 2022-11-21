fileObject = open("data_original/data.txt", "r")

data = []

while (True):
    line = fileObject.readline()
    if not line:
        break
    data.append(line)
    # print(line)

third_down = []
fourth_down = []
left_count = 0
middle_count = 0
right_count = 0

for line in data:
    string = line.split(" ")
    for word in string:
        if word == "left":
            left_count += 1
        if word == "right":
            right_count += 1
        if word == "middle":
            middle_count += 1
    rd = line.find('3rd &')
    th = line.find('4th &')

    str = ''
    if line[rd + 6: rd + 8] == 'Go':
        rd = line.find('3rd & Goal at')
        third_down.append(line[rd + 17: rd + 19].strip())
        str += ("third: " + line[rd + 17: rd + 19])
    else:
        third_down.append(line[rd + 6: rd + 8].strip())
        str += ("third: " + line[rd + 6: rd + 8])

    if line[th + 6: th + 8] == 'Go':
        th = line.find('4th & Goal at')
        fourth_down.append(line[th + 17: th + 19].strip())
        str += ("fourth: " + line[th + 17: th + 19])
    else:
        fourth_down.append(line[th + 6: th + 8].strip())
        str += ("fourth: " + line[th + 6: th + 8])
    # print(str)

rd_sum = 0
th_sum = 0
for num in third_down:
    if num[-1] == '\'':
        num = num[0:len(num) - 1]
    rd_sum += int(num)

for num in fourth_down:
    if num[-1] == '\'':
        num = num[0:len(num) - 1]
    th_sum += int(num)

print("Left:", left_count, "Middle:", middle_count, "Right:", right_count, "Average 3rd down:", round(rd_sum/len(third_down),1), "Average 4th down:", round(th_sum/len(fourth_down),1))
