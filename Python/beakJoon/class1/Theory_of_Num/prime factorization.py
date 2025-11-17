A = int(input())
answer = []
for i in range(2,A+1):
    if A%i == 0:
        answer.append(i)
        A = A / i
        print(A,answer)
print(answer)