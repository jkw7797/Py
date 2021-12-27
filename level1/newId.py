import re
def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    answer = re.sub('[^a-z0-9-_.]', '', answer)
    # 3
    while True:
        if answer.find("..") == -1:
            break
        answer = answer.replace("..", ".")
    # 4
    while True:
        if len(answer)<1:
            break
        if answer[0]!=".":
            break
        answer=answer[1:]

    while True:
        if len(answer)<1:
            break
        if answer[len(answer)-1]!=".":
            break
        answer=answer[:len(answer)-1]

    if answer == "":
        answer = "a"

    if len(answer)>=16:
        answer = answer[:14]
        while True:
            if answer[len(answer) - 1] != ".":
                break
            answer = answer[:len(answer) - 1]

    while len(answer)<3:
        answer+=answer[len(answer)-1]


    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))