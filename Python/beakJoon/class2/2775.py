Test_Case = int(input())
apartment = [[i for i in range(1,15)]]
for i in range(Test_Case):
    k = int(input())
    n = int(input())
    for j in range(1,k+1): #층 수 
        apartment.append([])
        total = 0 
        for p in range(n): # 사람 수
            total += apartment[j-1][p]
            apartment[j].append(total)
    print(apartment[k][n-1])
    apartment = [[i for i in range(1,15)]]


