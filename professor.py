

n , m , k = input().split(' ')



kharabia = []
matrix = []
for j in range(int(n)):
    satr =[]
    for l in range(int(m)):
        satr.append(1)
    matrix.append(satr)

for i in range(int(k)):
    
    r , c = input().split(' ')
    matrix[int(r)-1][int(c)-1] = 0
    
    




if ((int(k)%2) != 0):
    print(0)
    
elif (int(k) >= (int(n)*int(m))):
    print(-1)
    
else:
    damaged = []
    for i in matrix:
        for j in i:
            if (j != 0):
                damaged.append(matrix.index(i)+1)
                damaged.append(i.index(j)+1)
                break
    print(1)
    print(damaged[0] , damaged[1])
    
