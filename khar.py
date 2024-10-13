


n , m = input().split(' ')

loghat = {}

for i in range(int(n)):
    question , answer = input().split(' ')
    loghat[question] = answer 
    
    
bozQuestion = input().split(' ')
allQuestions = loghat.keys()
answer = []

for i in bozQuestion:
    if (i in allQuestions):
        answer.append(loghat[i])
        answer.append('kachal!')
    else:
        answer.append('kachal!')



lastAnswer = " ".join(str(x) for x in answer)
print(lastAnswer)