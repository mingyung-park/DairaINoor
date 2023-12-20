from sys import stdin
from collections import deque

n,k=map(int, stdin.readline().split())

visited=[False]+[False]*max(n,k)*2
dq=deque()
dq.append(n)
time = 0
def dfs(dq,k):
    next_dq=deque()
    check = 0
    while dq:
        now = dq.popleft()
        if(not visited[now]):
            visited[now]=True
            if(now==k):
                check=-1
                break 
            for i in [-1,1,now]:
                target=i+now
                if(0<=target<=2*k and visited[target]==False):
                    next_dq.append(target)
                    check+=1
    return check,next_dq

if(n>=k):
    print(n-k)
else:
    while dq:
        count,dq = dfs(dq,k)
        if(count!=-1):
            time+=1
        if(count==-1):
            break

    print(time)