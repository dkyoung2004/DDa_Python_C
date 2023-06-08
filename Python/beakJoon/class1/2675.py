a = int(input())

for i in range(0,a):
    literate , target = input().split()
    text = ''
    for j in target:
        text += j * int(literate)
    print(text)