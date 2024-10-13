



n , x , y = input().split(' ')


a = input().split(' ')

n2 = int(n)-1


ai = [int(x) for x in a]

lastai = min(ai)

ai.remove(lastai)
ai.sort(reverse=True)

lastResault = []
for i in ai:
    while True:
        diffrent = 100-i
        if (diffrent <= 0 or lastai < int(x)):
            break;
        else:
            lastai -= int(x)
            i += int(y)
    lastResault.append(i)
    
    
# print(lastResault)

if ((sum(lastResault)/len(lastResault)) >= 100):
    print('YES')
else:
    print('NO')
        
            

