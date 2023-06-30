N = int(input())
Loop = N-1


for i in range(-Loop,Loop+1):
    for j in range(0,abs(i)):
        print(" ",end="")
    for j in range(0,((2*N-1)-(2*abs(i)-1))-1):
        print("*",end="")

    print("")