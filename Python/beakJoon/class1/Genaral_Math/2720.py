N = int(input())
Quarter = Dime = Nickel = Penny = 0
Change = 0
for i in range(0,N):
    Change = int(input())
    Quarter = Dime = Nickel = Penny = 0
    while(Change > 0 ):
        if(Change >= 25):
            Quarter +=1
            Change -= 25
        elif(Change >= 10):
            Dime += 1
            Change -=10
        elif(Change >= 5):
            Nickel += 1
            Change -= 5
        else:
            Penny +=1
            Change-=1
    print(Quarter,Dime,Nickel,Penny)