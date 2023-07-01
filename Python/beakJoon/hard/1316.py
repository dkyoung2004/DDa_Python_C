N=int(input())
count = 0
for i in range(0,N):
    Text=list(str(input()))
    a=True
    Array_group = set()
    for j in range(0,len(Text)):
        if ((Text[j] in Array_group) and (Text[j] != Text[j-1])):
            a = False
        else:
            Array_group.add(Text[j])
    if(a):
        count+=1
print(count)