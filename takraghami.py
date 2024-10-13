



x = input()

x = list(x)

s = [int(i) for i in x]



summ = 0

while True:
    
    summ = sum(s)
    if (summ < 10):
        break;
    else:
        ll = list(str(summ))
        s = [int(i) for i in ll]
       


print(summ)
         