a = []
N =  int(input())
spare = 0
spare2 = 0
for i in range(0,N):
    a.append(i+1)
for i in range(0,N-1):
    del a[0]
    spare = a[0]
    spare2 = a[(int(len(a))-1)]
    a[0] = spare2
    a[(int(len(a))-1)] =spare
    print(a)
print(a)
