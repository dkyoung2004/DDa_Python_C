A_quantity , B_quantity = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

result = (A-B).union(B-A)
print(len(result))