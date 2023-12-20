from sys import stdin
from collections import deque

n,k=map(int, stdin.readline().split())

visited=[0]+[0]*max(n,k)*2
dq=deque()
dq.append(n)
time = 0
visited[n]=1
def dfs(dq,k):
    next_dq=deque()
    check = 0
    print(dq)
    while dq:
        now = dq.popleft()

        if(now==k):
            check+=1 
    
        for i in [-1,1,now]:
            target=i+now
            if 0<=target<=2*k and (visited[target]==0 or visited[target]==visited[now]+1):
                visited[target]=visited[now]+1
                next_dq.append(target)
    return check,next_dq

if(n>=k):
    print(n-k)
    print(1)

else:
    while dq:
        count,dq = dfs(dq,k)
        if(count==0):
            time+=1
        else:
            break

print(time)
print(count)