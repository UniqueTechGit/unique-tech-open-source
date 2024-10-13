


a , b , c = input().split(' ')


s = [int(a) , int(b) , int(c)]

maximum = max(s)
middle = sum(s)/len(s)
s.remove(maximum)
counter = 0

for i in s:
    if (i < maximum):
        diffrent = middle - i  
        maximum -= diffrent
        i += diffrent
        counter += 1
        
        

print(counter)
            