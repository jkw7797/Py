import collections


def solution1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]



def solution(participant, completion):
    participant.sort() #정렬
    completion.sort()


    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = 	["josipa", "filipa", "marina", "nikola"]
answer = solution1(participant,completion)
print(answer)