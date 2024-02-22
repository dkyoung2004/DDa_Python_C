arr = list(input())
inn = set()
value = ''
for i in range(len(arr)):
    for j in range(i,len(arr)):
        value += arr[j]
        inn.add(value)
    value = ''
print(len(inn))
