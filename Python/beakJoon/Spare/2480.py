a =b =c =0
a,b,c =map(int,input().split())
Prize = 0
Highest = 0
if (a == b == c):
    Prize = 10000+(a*1000)
elif (a==b):
    Prize = 1000+(a*100)
elif (b==c):
    Prize = 1000+(b*100)
elif (c==a):
    Prize = 1000+(c*100)
else:
    if(a > b) and (a>c):
        Highest = a
    elif(b > a) and (b>c):
        Highest = b
    else:
        Highest = c 
    Prize =  Highest * 100

print(Prize)

