N = str(input())
N = list(N)

Count = 0
for i in range(0,len(N)):
    if(i>=1):
        if(N[i] == "j" and (N[i-1] == "n" or N[i-1] == "l")):
            Count += 1
        if((N[i] == "=") and (N[i-1]== "c" or N[i-1] == "s" or N[i-1]== "z")):
            Count+=1
        if((N[i] == "-") and (N[i-1]=="c" or N[i-1]=="d")):
            Count += 1
        if( N[i]=="z"and N[i+1]=="=" and N[i-1] == "d"):
            Count +=1
print(len(N)-Count)