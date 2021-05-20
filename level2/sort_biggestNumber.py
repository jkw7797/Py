def solution(numbers):
    num_list = list(map(str, numbers))
    num_list = sorted(num_list,key = lambda x:x*3, reverse=True)
    answer = str(int(''.join(num_list)))
    return answer


numbers =[6, 10, 2]
print(solution(numbers))