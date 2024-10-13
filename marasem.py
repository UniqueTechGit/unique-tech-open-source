


n = int(input())


giftLists = {}
for i in range(n):
    
    giftLists[input()] = 0
    





for i in range(n):
    name = input()
    money , k = input().split(' ')
    giftLists[name] -= int(money)
    if (int(k) != 0):
        perGift = int(money) // int(k)
        backMoney = int(money) % int(k)
        for j in range(int(k)):
            giftLists[input()] += perGift
        giftLists[name] += backMoney    
    else:
        giftLists[name] += int(money)
    
    

for i in (giftLists.keys()):
    print(i , giftLists[i])   
    