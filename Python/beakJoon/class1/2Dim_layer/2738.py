I , J = map(int,input().split())
array_1 = []
array_2 =[]
for i in range(0,I):
    array_1.append(list(map(int,input().split())))
for i in range(0,I):
    array_2.append(list(map(int,input().split())))
for i in range(0,I):
    for j in range(0,J):
        print(array_1[i][j]+array_2[i][j],end=" ")
    print("")

