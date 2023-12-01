def solution(x):
    sum = 0
    temp = x
    while(temp >= 10):
        sum += temp % 10
        temp = temp // 10
        
    sum += temp
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer