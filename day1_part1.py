
data = []

with open("inputDay1.txt", 'r') as file:
    data = file.readlines()

totalSum = 0

leftValues = []
rightValues = []

for dataPoint in data:
    
    values = dataPoint.strip().split("   ")

    leftValues.append(int(values[0]))
    rightValues.append(int(values[1]))

leftValues.sort()
rightValues.sort()

for index in range(len(data)):
    totalSum += abs(leftValues[index] - rightValues[index])

print(totalSum)
