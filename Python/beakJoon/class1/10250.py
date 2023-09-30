from string import ascii_lowercase

S = list(map(str,input()))

alpha = list(ascii_lowercase)

for i in alpha:
    if( i in S):
        print(S.index(i), end = ' ')
    else:
        print(-1, end=' ') 