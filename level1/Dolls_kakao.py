def solution(board, moves):
    x=[]
    count =0
    for i in moves:
        move = i-1
        j=0
        while j < len(board)-1:
            doll = board[j][move]
            if(doll != 0):
                board[j][move] = 0
                x.append(doll)
                if len(x) >= 2:
                    if x[len(x)-1] == x[len(x)-2]:
                        count += 2
                        x.pop()
                        x.pop()
                    break
            j+=1

    return count


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
answer = solution(board, moves)
print(answer)