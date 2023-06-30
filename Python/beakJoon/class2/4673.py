def Self_Number (a):
    #https://kbwplace.tistory.com/69 코드 참고함
    Output = a + sum(map(int,str(a)))
    return Output
Self_set= set(range(1,10001))
remove_set = set()
for i in range(1,10001):
    remove_set.add(Self_Number(i))

b = Self_set - remove_set
b = sorted(b)
for i in range(0,len(b)):
    print(b[i])