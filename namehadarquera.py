



n , m = input().split(' ')


l = input().split(' ')


if (int(n) == 1 or int(m) == 1):
    print('NO')
    
else:
    if ((int(n)% int(m) == 0)):
        print("YES")
    else:
        print("NO")