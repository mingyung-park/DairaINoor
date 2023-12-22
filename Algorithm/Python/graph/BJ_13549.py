from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
check = [float('inf')] * (max(n,k)*2+1)
check[n] = 0
search_q = deque([n])
flag =False
def bfs(search_q,check):
    flag=False
    next_q = deque()

    while search_q:
        now = search_q.popleft()
        
        if now==k:
            flag=True
        
        for i in [-1, 1, 2]:
            next_idx = now + i if i != 2 else now * i
            sumation = 0 if i==2 else 1
        
            if 0<=next_idx<=2*k:
                if check[next_idx]>=(check[now]+sumation): #방문 가능한 경우
                    check[next_idx]=check[now]+sumation
                    next_q.append(next_idx)
    
    return next_q, flag
 
                

if(n>=k):
    print(n-k)
else:
    while not flag:
        search_q, flag=bfs(search_q,check)
    print(check[k])

        