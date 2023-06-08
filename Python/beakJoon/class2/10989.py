numer = int(input())
a = []
for i in range(0,numer):
    a.extend(input())

def insertionSort(List,n):
    a= 0
    for i in range(1,n):
        key = List[i]
        for j in range(i,-1,-1):
            if key < List[j]:
                List[j+1]=List[j]
                List[j]=key
    return List

print(insertionSort(a,numer))

