

n = input()

c = input().split(' ')

q = int(input())

# print(q)

question = []
for i in range(q):
        question2 = input().split(' ')
        question.append(question2)
        

resultForCheck = []
for j in question:
    # print('j>>>' , j)
    start = int(j[0])
    end = int(j[1])
    # print('j>>>' , int(j[1]))
    sum = 0
    Range = []
    truely = 0;
    for k in range(start , end+1):
        # print( 'print', k)
        sum += int(c[k-1])
        Range.append(int(c[k-1]))
        
        #! here has a problem...
    for h in range(1 , sum+1):
        if h in Range:
            truely += 1
             
        else:
            for k in Range:
                for l in range(Range.index(k)+1 , len(Range)):   #! its just sum two of the elements
                    if (Range[l] + k == h):
                        truely += 1
                        
                        
    print(sum , truely)
    if (truely == sum):
        resultForCheck.append('PERFECT')
    else:
        resultForCheck.append('NOT PERFECT')
        
        
print(resultForCheck)
                    
                  
      
      
      
#!greedy algorithmmmmm

i = 0
newList = arange
sumList = []
while True:
    maximum = max(newList)
    newList.remove(maximum)
    sumList.append(maximum)
    if (sum(sumList) == myNum):
        break
    
    if (sum(sumList) > myNum):
        sumList.remove(sumList[-1])
        i += 1
        
    elif (sum(sumList) < myNum):
        i += 1
   