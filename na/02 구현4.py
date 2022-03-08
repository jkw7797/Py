#문자열 재정렬
#알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
#EX) K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

#문자열이 입력되었을 때 문자를 하나씩 확인
#숫자인 경우 따로 합계를 계산
#알파벳의 경우 별도의 리스트에 저장
#->리스트에 저장된 알파벳을 정렬, 합계를 뒤에 붙여 출력

data = input()
result = []
value = 0
for x in data:
    if x.isalpha(): #알파벳일 경우 result리스트에 추가
        result.append(x)
    else: #숫자의 경우 value에 더해줌
        value += int(x)
result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))
