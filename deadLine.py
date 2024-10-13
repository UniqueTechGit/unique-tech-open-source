


n = int(input())

l , r = input().split(' ')

RANGE = []

for i in range(int(l) , int(r)+1):  
    RANGE.append(i)


RANGE.sort(reverse = True)    


def greed(array , k):
    pass
    
            

finalResault = greed(RANGE , n)

print(finalResault)