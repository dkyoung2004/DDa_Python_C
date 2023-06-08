a = []
b = [0 for k in range(42)]
count = 0
for i in range(0,10):
    a.append((int(input()))%42)
for j in range(0,10):
    b[a[j]] += 1
for q in range(0,42):
    if b[q] != 0:
        count+=1
print(count)