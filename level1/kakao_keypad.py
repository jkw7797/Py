# numbers 배열의 크기는 1 이상 1,000 이하입니다.
# numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# hand는 "left" 또는 "right" 입니다.
# "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 \
# 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.


def solution(numbers, hand):
    key_dist={1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    leftList = [1,4,7,"*"]
    rightList = [3,6,9,"#"]
    midList = [2,5,8,0]
    answer = ''
    pointL = '*'
    pointR = '#'
    for i in numbers:
        if i in leftList:
            answer += "L"
            pointL = i
        elif i in rightList:
            answer += "R"
            pointR = i
        else:
            key = key_dist[i]
            l = key_dist[pointL]
            r = key_dist[pointR]
            lDis = abs(l[0]-key[0])+abs(l[1]-key[1])
            rDis = abs(r[0] - key[0]) + abs(r[1] - key[1])


            point = midList.index(i)
            if lDis == rDis:
                if hand == "right":
                    answer += "R"
                    pointR = i
                else:
                    answer += "L"
                    pointL = i

            elif lDis < rDis:
                answer += "L"
                pointL = i
            else:
                answer += "R"
                pointR = i

    return answer

numbers = 	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
answer = solution(numbers, hand)
print(answer)

# "LRLLLRLLRRL"