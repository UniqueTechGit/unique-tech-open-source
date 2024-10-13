



n = int(input())

x = [x+1 for x in range(n)]


x.sort(reverse = True)
jigh = 2
x.remove(1)

# print(x)

inUsed = [1]

for i in range(len(x)):
    
    if (x[i] > max(inUsed) or x[i] < min(inUsed)):
        jigh += 1
    inUsed.append(x[i])


print(jigh)

    