def solution(s):
    word={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5',
          'six':'6','seven':'7','eight':'8','nine':'9'}
    answer = ""
    a=""
    for i in s:
        if i.isdigit():
            answer +=i
        else:
            a+=i
            if a in word.keys():
                answer += word[a]
                a=""

    return int(answer)


txt= "23four5six7"
print(solution(txt))

