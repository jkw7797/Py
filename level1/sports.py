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
