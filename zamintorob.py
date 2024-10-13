

n , m , s = input().split(' ')



if(int(s) >= int(n) or int(s) >= int(m)):
    if (int(s) >= int(n)):
        diff = int(s)-int(n)
        if (diff % 2 == 0):
            print('possible')
            for i in range(int(n)):
                
            
    elif (int(s) >= int(m)):
        diff = int(s)-int(m)
        if (diff % 2 == 0):
            print('possible')
    
else:
    if (int(s) == 1 and ((int(n)%2) != 0 or (int(m)%2)!= 0)):
        print('possible')
    else:
        print('impossible')
    
