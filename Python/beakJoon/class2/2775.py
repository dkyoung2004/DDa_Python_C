Test_Case = int(input())
apartment = [[i for i in range(1,14)]]
for i in range(Test_Case):
    k = int(input())
    n = int(input())
    for j in range(1,k+1): #층 수 
        apartment.append([])
        total = 0
        for p in range(n): # 사람 수

            print("this is p:",p)

            for m in range(n): #아랫층 호수까지의 합
                print("this is m:",m)
                total += apartment[j-1][m]
            print("this is total:",total)
            apartment[j].append(total)
    print(apartment)
    print(apartment[k][n-1])


