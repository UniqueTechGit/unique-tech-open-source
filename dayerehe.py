

import math

n = int(input())


coordination = []
maximum = 0
maximum1 = 0
for i in range(n):
    x , y = input().split(' ')
    if (int(x) > maximum):
        maximum = int(x)
    if (int(y) > maximum1):
        maximum1 = int(y)
    coordination.append([int(x) , int(y)])
    


def formula(numbers):
    finalResault = []
    for i in range(numbers[5]):
        y = i
        firstSide = math.sqrt(((numbers[1] - numbers[0])**2) + ((numbers[3] - y)**2))
        secondSide = math.sqrt(((numbers[2] - numbers[0])**2) + ((numbers[4] - y)**2))
        print('ff',firstSide)
        print('ss',secondSide)
        if (firstSide == secondSide):
            finalResault = [numbers[0] , y]
    # print(finalResault)
    return [finalResault , firstSide]
    
    

lastResault = []

for j in range(maximum):
    totalCheck = 0
    choosenX = j + 1
    cord1 = coordination[0]
    cord2 = coordination[1]
    res = formula([choosenX , cord1[0] , cord2[0] , cord1[1] , cord2[1] , maximum1])
    if (res[0] != []):
        for i in coordination:
            distance = math.sqrt(((i[0] - res[0][0])**2) + ((i[1] - res[0][1])**2))
        if (distance == res[1]):
            totalCheck += 1
        if (totalCheck == len(coordination)):
            lastResault = res[0]
        


print('last',lastResault)

    
    

    

