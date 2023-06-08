a = int(input())
b = input()
print(type(b))
b_list = list(map(int,str(b)))
sigma = 0
for i in range(0,a):
    sigma += b_list[i]
print(sigma)