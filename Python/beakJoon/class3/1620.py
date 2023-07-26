import sys
input = sys.stdin.readline


N, M = map(int,input().split())

pocketMon = {}
for i in range(1,N+1):
    code = str(input())
    new_code = code.replace("\n","")
    pocketMon[i] = new_code
    pocketMon[new_code] = i
for i in range(0,M):
    code = input().rstrip()
    if code.isalpha():
        print(pocketMon[code])
    else:
        print(pocketMon[int(code)])

    

    
