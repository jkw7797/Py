def sol(n, movePlan):
    import time
    start_time = time.time()

    man = [1, 1]
    moveR = [0, 1]
    moveL = [0, -1]
    moveU = [-1, 0]
    moveD = [1, 0]

    for i in movePlan:
        if i == 'R':
            man[0] += moveR[0]
            man[1] += moveR[1]
        elif i == 'L':
            man[0] += moveL[0]
            man[1] += moveL[1]
        elif i == 'U':
            man[0] += moveU[0]
            man[1] += moveU[1]
        elif i == 'D':
            man[0] += moveD[0]
            man[1] += moveD[1]

        if man[0] < 1:
            man[0] = 1
        elif man[0] > n:
            man[0] = 5

        if man[1] < 1:
            man[1] = 1
        elif man[1] > n:
            man[1] = 5
        # print(man)

    end_time = time.time()  # 측정 종료
    print("time: ", end_time - start_time)  # 수행시간 출력

    return man
print(sol(100,"RRRRRUDDRRRUDDRRRUDDRUDDRRUDDRRRUDDRRRUDDRRRUDDRRRUDDRUDRRRRRUDDRRRUDDRRRUDDRUDDRRUDDRRRUDDRRRUDDRRRUDDRRRUDDRUDDRRRRRUDDRRRUDDRRRUDDRUDDRRUDDRRRUDDRRRUDDRRRUDDRRRUDDRUDDD"))

