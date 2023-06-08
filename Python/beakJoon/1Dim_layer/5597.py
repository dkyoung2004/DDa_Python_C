a = []
variable = 0

for j in range(1,31):
    a.append(j)
for i in range(0,28):
    variable = int(input())
    a.remove(variable)
print(a[0])
print(a[1])