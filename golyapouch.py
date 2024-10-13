


x , n = input().split(' ')

currentPosition = n

for i in range(int(x)):
    changePosition = input().split(' ')
    if (currentPosition in changePosition):
          changePosition.remove(currentPosition)
          currentPosition = changePosition[0]
          
          
          
print(currentPosition)