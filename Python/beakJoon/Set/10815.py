N = int(input())

list_Sang = list(map(int, input().split()))

M = int(input())

list_Target=list(map(int, input().split()))
set_Target = set(list_Target)
set_Sang = set(list_Sang)
result = set_Sang & set_Target
for i in list_Target:
    if( i in result):
        print(1,end =" ")
    else:
        print(0,end = " " )