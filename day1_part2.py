
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



rightIndex = 0
leftIndex = 0

totalValCount = len(leftValues)
while leftIndex < totalValCount:

    leftValCount = 1

    currentVal = leftValues[leftIndex]

    while (leftIndex + 1 < totalValCount and currentVal == leftValues[leftIndex + 1]):
        leftValCount += 1
        leftIndex += 1
    

    while (rightIndex < totalValCount and currentVal >= rightValues[rightIndex]):
        if (rightValues[rightIndex] == currentVal):
            totalSum += currentVal * leftValCount
        rightIndex += 1

    leftIndex += 1
        

print(totalSum)
