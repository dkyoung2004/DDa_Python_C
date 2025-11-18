ISBN = list(map(str,input()))

mod = ISBN.pop()
mod = ((10 - int(mod))%10)
SUM = 0
a = ISBN.index("*")
ISBN[a] = 0

ISBN = list(map(int,ISBN))
for i in range(len(ISBN)):
    if(i % 2) == 1:
        SUM += ISBN[i] *3
    else:
        SUM += ISBN[i]
temp = SUM
if (a % 2) == 1:
    for i in range(10):
        temp = SUM + (i*3)
        if (temp % 10) == mod:
            print(i)
else:
    for i in range(10):
        temp = SUM + i
        if (temp % 10) == mod:
            print(i)
