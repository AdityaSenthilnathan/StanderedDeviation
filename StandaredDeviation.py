import csv
import math
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
datafull = 0
for f in data:
    datafull = datafull + int(f)

mean = datafull/len(data)

print(mean)
length = 0
sumofAll = 0
for d in data:
    subval = int(d) - mean
    sqrval = subval * subval
    length = length + 1
    sumofAll = sumofAll + sqrval


divval = sumofAll/len(data)

finalVal = math.sqrt(divval)
print(finalVal)