from collections import deque

def solution(priorities, location):
    index_pri = [i for i in range(len(priorities))]
    pri = priorities.copy()
    i=0
    while(True):
        if pri[i] < max(pri[i+1:]):
            index_pri.append(index_pri.pop(i))
            pri.append(pri.pop(i))
        else:
            i+=1
        if sorted(pri,reverse=True) == pri:
            break

    return index_pri.index(location)+1

def solution2(priorities, location):
    deq = deque()



priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))