




n = int(input())


ai = []
unsorted = []

for j in range(n):
    unsorted.append(j+1)
    


for i in range(n):
    ai.append(int(input()))

ai.reverse()
unsorted.sort(reverse = True)

for k in ai:
    firstIndex = ai.index(k)
    secondIndex = unsorted.index(unsorted[firstIndex])
    if (secondIndex != k):
        replace = unsorted[k]
        first = unsorted[ai.index(k)]
        unsorted[unsorted.index(first)] = replace 
        unsorted[unsorted.index(replace)] = first 
    


print(ai)
print(unsorted)

    

