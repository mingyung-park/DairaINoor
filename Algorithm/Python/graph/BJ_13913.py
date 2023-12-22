from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
check = [float('inf')] * (max(n,k)*2+1)
check[n] = 0
search_q = deque()
search_q.append(deque([n]))
flag =False
ans = deque()

def bfs(search_q,check):
    flag=False
    next_q = deque()

    while search_q:
        now_q = search_q.popleft()
        now=now_q.popleft()
        if now==k:
            flag=True
            ans.appendleft(now_q)
            
        for i in [-1, 1, 2]:
            next_idx = now + i if i != 2 else now * i
            sumation = 1
        
            if 0<=next_idx<=2*k:
                if check[next_idx]>=(check[now]+sumation): #방문 가능한 경우
                    check[next_idx]=check[now]+sumation
                    
                    temp=deque(now_q)
                    temp.appendleft(now)
                    temp.appendleft(next_idx)
                    
                    next_q.append(temp)
    
    return next_q, flag
 
                

if(n>=k):
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end =" ")

else:
    while not flag:
        search_q, flag=bfs(search_q,check)
    print(check[k])
    answer = ans.pop()
    answer.appendleft(k)
    for i in range(len(answer)):
        print(answer.pop(), end=" ")

