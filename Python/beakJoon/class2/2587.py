arr = []

for _ in range(5):
    arr.append(int(input()))
arr.sort(reverse=True)

print(int((arr[0]+arr[1]+arr[2]+arr[3]+arr[4])/5))
print(arr[2])