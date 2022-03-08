#곱하기 혹은 더하기
#주어진 숫자 +,*로 크게 만들기
data = input()
#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for  i in range(1,len(data)):
    num = int(data[i])
    # num이나 result 중 1보다 작은 수(0 or 1)가 있다면 더하기로 아니라면 곱하기
    if num <= 1 or result <=1:
        result +=num
    else:
        result *= num
print(result)
