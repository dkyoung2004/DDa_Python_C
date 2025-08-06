import sys

input = sys.stdin.readline

a = int(input())
a_sort =  a // 10

if a_sort >= 9 :
    print("A")
elif a_sort == 8:
    print("B")
elif a_sort == 7:
    print("C")
elif a_sort == 6 :
    print("D")
else:
    print("F")