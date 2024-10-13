

n , k=input().split(' ')

friends = input().split(' ')

total = [int(x)+1 for x in friends]

confirmed = []

summ = 0

total.sort()
for i in total:
    if(summ + i <= int(k)):
        summ += i
        confirmed.append(i)
    

print(len(confirmed))