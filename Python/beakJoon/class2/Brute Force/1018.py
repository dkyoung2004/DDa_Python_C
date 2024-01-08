N,M = map(int,input().split())
list_board = []
check_set_1= [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
check_set_2= [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],]
Min = 64
loop=0
for i in range(0,N):
    list_board.append([])
    list_board[i]=list(str(input()))
for i in range(0,N-7):
    for j in range(0,M-7):
            count_1 = 0
            count_2 = 0
            for l in range(0,8):
                for o in range(0,8):
                    if(check_set_1[l][o] != list_board[i+l][j+o]):
                        count_1+=1
                    if(check_set_2[l][o] != list_board[i+l][j+o]):
                        count_2+=1
            if(count_1 > count_2):
                count_1 = count_2
            if(count_1 < Min):
                Min = count_1
print(Min)