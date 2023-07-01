N=input()
Count = 0
key_croatia = ['c=','c-','lj','dz=','nj','s=','z=','d-']
for i in key_croatia:
    N = N.replace(i,'*')
print(len(N))