N , M = map(int, input().split())
Include_String = []
Check_String = []
for i in range(0,N):
    Include_String.append(str(input()))
Include_String = set(Include_String)
var = 0
for i in range(0,M):
    if(str(input()) in Include_String):
        var+=1
print(var)


