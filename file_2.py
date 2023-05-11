def solution(number):
    sum = 0
    
    for num in range(number):
        if num % 5 == 0 and num % 3 == 0:
            sum += num
        elif num % 5 == 0:
            sum += num
        elif num % 3 == 0:
            sum += num
            
    return sum

print(solution(150))