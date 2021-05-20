def solution(numbers):
    num_list = list(map(str, numbers))
    num_x = list(map(str, numbers))
    print(num_list)
    num_list = sorted(num_list,key = lambda x:x*3, reverse=True)
    print(num_list)
    num_x.sort(key=lambda x : x*3,reverse=True)
    print(num_x)
    num_y = list(map(lambda x : x*3, num_list))
    print(num_y)

    answer = str(int(''.join(num_list)))
    return answer


numbers =[6, 10, 2]
print(solution(numbers))