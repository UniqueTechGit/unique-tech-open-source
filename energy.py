# import time

# time1 = time.time()

n , k = input().split(' ')

k = int(k)

loseEnergy = []

giveEnergy = []


for i in range(int(n)):
    lose , give = input().split(' ')
    loseEnergy.append(int(lose))
    giveEnergy.append(int(give))
    
    
loseEnergy.sort(reverse = True)
giveEnergy.sort(reverse = True)


while (len(giveEnergy) > 0):
    for i in giveEnergy:
        if (i <= k):
            index = giveEnergy.index(i)
            k -= loseEnergy[index]
            k += i
            loseEnergy.remove(loseEnergy[index])
            giveEnergy.remove(i)

# time2 = time.time()
# print(time2-time1)
print(k)