n = int(input())
text = []

for i in range(0,n):
    text.append(input())
a = list(set(text))
a.sort()
a = sorted(a,key = len)
for j in range(0,len(a)):
    print(a[j])
