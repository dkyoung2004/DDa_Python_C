X_1 , Y_1 = map(int,input().split())
X_2 , Y_2 = map(int,input().split())
X_3 , Y_3 = map(int,input().split())

list_X = [X_1,X_2,X_3]
list_Y = [Y_1,Y_2,Y_3]

for i in list_X:
    if(list_X.count(i) ==1):
        print(i,end=" ")
for i in list_Y:
    if(list_Y.count(i)==1):
        print(i)