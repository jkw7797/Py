# def solution(n, lost, reserve):
#     for i in reserve[:]:
#         if i in lost:
#             lost.remove(i)
#             reserve.remove(i)
#
#     for i in reserve:
#         if i - 1 in lost:
#             lost.remove(i-1)
#             continue
#         elif i + 1 in lost:
#             lost.remove(i+1)
#             continue
#
#     result = n - len(lost)
#
#     return result

2
3
4
5
6
7
8
9
10
11
12
13


def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        if l-1 in reserveN:
            reserveN.remove(l-1)
            reserved += 1
        elif l+1 in reserveN:
            reserveN.remove(l+1)
            reserved +=1
    return n - len(lostN) + reserved


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))

#
# def solution(n, lost, reserve):
#     for i in lost:
#         if (i in reserve):
#             reserve.remove(i)
#             lost.remove(i)
#
#         if not reserve:
#             break
#
#     result = n - len(lost)
#     answer = 0
#     if not lost:
#         return result
#
#     for i in lost:
#         if not reserve:
#             break
#         if (i - 1) in reserve:
#             result += 1
#             reserve.remove(i - 1)
#         elif (i + 1) in reserve:
#             result += 1
#             reserve.remove(i + 1)
#
#     return result
