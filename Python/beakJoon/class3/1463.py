X= int(input())
loop = [0] * (X+1)
for i in range(2,X+1):
    loop[i] = loop[i-1]+1
    if i%2==0:
        loop[i] = min(loop[i], loop[i//2]+1)
    elif i%3==0:
        loop[i] = min(loop[i],loop[i//3]+1)
    print(loop)
print(loop[X])