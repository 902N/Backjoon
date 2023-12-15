def solution(n, s):
    if n > s:
        answer = [-1]
        return answer
    
    answer = []
    quotient = s // n
    remainder = s % n
    for i in range(n):
        answer.append(quotient)
    for i in range(remainder):
        answer[i] += 1
    answer.sort()
    return answer