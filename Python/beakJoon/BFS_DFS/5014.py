from collections import deque


F , S, G , U, D = map(int,input().split())
visited = [ 0 for _ in range(1000000+1)]
def BFS():
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        x = q.popleft()
        if x == G:
            return (visited[x]-1)
        else:
            if((x+U)>0) and ((x+U) <=F) and (visited[x+U] == False):
                q.append(x+U)
                visited[x+U] += visited[x]+1
            if((x-D)>0)and ((x-D) <=F) and ( visited[x-D] == False):
                q.append(x-D)
                visited[x-D] += visited[x]+1
    return "use the stairs"
        
print(BFS())