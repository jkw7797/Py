#모험가 길드
n = int(input("모험가 수"))
data = list(map(int, input("공포도").split()))
data.sort()

result = 0
count = 0

for i in data:
    count +=1
    if count >= i:
        result +=1
        count = 0

print(result)