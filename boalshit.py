
t = int(input())

lastAnswer = []


for i in range(t):
    ostani = 0
    keshvari = 0
    n = input().split(' ')
    ranks = input().split(' ')
    p = input().split(' ')
    R = int(input())
    
    minimum7 = 0
    
    for i in n:
        if (int(i) >= 7):
            minimum7 += 1
   
    if (minimum7 == len(n)):    
        for j in n:
            index = n.index(j)
            if (int(j) >= 7):
                if (int(ranks[index]) == 1):
                    if (int(p[index]) >= 2):
                        ostani = 1
        
        if (R <= 40):
            keshvari = 1
        if (keshvari == 1 or ostani == 1):
            lastAnswer.append('YES')
        else: 
            lastAnswer.append('NO')
        
    else : 
        lastAnswer.append('NO')
    


for i in lastAnswer:
    print(i)
    