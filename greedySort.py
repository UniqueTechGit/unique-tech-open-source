

t = int(input())

varss = []

for i in range(t):
    n = int(input())
    variables = input().split(' ')
    varss.append([int(x) for x in variables])


def padding(array):
    
    usedBite = {}
    c = 0
    while (len(array)>0):
        
        maximum = max(array)
        usedBite[str(c)] = [maximum]
        array.remove(maximum)
        for i in array:
            if ((i + maximum) <= 4):
                usedBite[str(c)].append(i)
                array.remove(i)
        c += 1
    
    paddingSpaces = 0
    keys = list(usedBite.keys())
    for j in range(len(keys)-1):
        paddingSpaces += (4 - sum(usedBite[keys[j]]))
        
    return (paddingSpaces)


resault = []

for i in varss:
    resault.append(padding(i))
  
for i in resault:
    print(i)
   

    
    