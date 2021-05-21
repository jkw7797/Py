def solution(citations):
    sor_citations = sorted(citations)
    index = int(len(sor_citations)/2)
    answer=0;
    count = 0;
    print(sor_citations[index:])
    print(sor_citations[:index])
    while(True):
        if (sor_citations[index] >= len(sor_citations[index:])):
            if(sor_citations[index] > sum(sor_citations[:index])):
                if(answer > sor_citations[index]):
                    return answer
                else:
                    answer = sor_citations[index]
            else:
                index -= 1
        else:
            index +=1

        count +=1
        if count > len(sor_citations):
            break;




citations = [3, 0, 6, 1, 5]
print(solution(citations))