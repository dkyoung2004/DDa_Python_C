array =[]
Max = 0
Max_location = [0,0]
for i in range(0,9):
    array.append(list(map(int,input().split())))
for i in range(0,9):
    for j in range(0,9):
        if(Max<=array[i][j]):
            Max=array[i][j]
            Max_location[0] = i+1
            Max_location[1] = j+1
print(Max)
print(Max_location[0],Max_location[1])
