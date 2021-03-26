import csv
import math

data = [60, 61, 65, 63, 98, 99, 90, 95, 91, 96]


def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total / n
    return mean


listOfSquaredNumbers = []

for number in data:
    n = int(number) - mean(data)
    n = n**2
    listOfSquaredNumbers.append(n)

sum = 0

for i in listOfSquaredNumbers:
    sum = sum + i

result = sum / (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)