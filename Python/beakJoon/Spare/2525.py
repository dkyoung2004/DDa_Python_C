H =0
M=0
Count=0

H,M = map(int, input().split())
Count = int(input())

H += int((M+Count)//60)
M = ((M+Count)%60)
if H >= 24:
    H -= 24

print(H, M)