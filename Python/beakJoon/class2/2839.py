N = int(input())
bonzzi = 10000
ear_bonzzi = 5000
i = 0
while(N>=0):
    if(N%5==0):
        ear_bonzzi = (N/5)
        ear_bonzzi += i
    elif(N%3==0):
        ear_bonzzi = (N/3)
        ear_bonzzi += i
    else:
        ear_bonzzi = bonzzi
    if(ear_bonzzi<bonzzi):
        bonzzi = ear_bonzzi
    N -= 3
    i += 1
    early_bonzzi = bonzzi

if(bonzzi == 10000):
    print(-1)
else:
    print(int(bonzzi))
    

