N = int(input())

Paper = [[0 for i in range(0,100)]for i in range(0,100)]
for i in range(0,N):
    x,y= map(int,input().split())

    for row in range(x,x+10):
        for col in range(y,y+10):
            Paper[row][col] = 1
result = 0
for i in Paper:
    result += i.count(1)
print(result)