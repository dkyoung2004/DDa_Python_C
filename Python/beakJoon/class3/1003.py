T = int(input())
def fibonacci(N):
    zero = [1,0,1]
    one = [0,1,1]
    length = len(zero)
    if N >= length:
        for i in range(2,N):
            zero.append(zero[i-1]+zero[i])
            one.append(one[i-1]+one[i])
    print('{} {}'.format(zero[N],one[N]))

for i in range(0,T):
    N =  int(input())
    fibonacci(N)

