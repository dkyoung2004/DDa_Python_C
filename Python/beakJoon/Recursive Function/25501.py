 

def recursion(s,l,r,t):
    global e
    t +=1
    e = t
    if(l >=r):
        return 1
    elif(s[l] != s[r]):
        return 0
    else:
        return recursion(s,l+1,r-1,t)
def isPalindrome(s):
    return recursion(s, 0 ,len(s)-1,0)

T = int(input())
for _ in range(T):
    s = list(map(str,input()))
    print(isPalindrome(s), e)