from sys import stdin
from collections import deque
m, n, h = map(int,stdin.readline().split())
non=0
tomato = []
queue = deque()
for i in range(h):
    tomato.append([])
    for j in range(n):
        tomato[i].append(list(map(int, stdin.readline().split())))
        for k in range(m):
            if(tomato[i][j][k]==1):
                queue.append([i,j,k])#z,y,x
            elif(tomato[i][j][k]==-1):
                non+=1
                
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
cnt = len(queue)
time=0

def bfs(now_q, cnt):
    next_q = deque()
    while now_q:
        now = now_q.pop()
        for i in range(6):
            sz = dz[i] + now[0]
            sy = dy[i] + now[1]
            sx = dx[i] + now[2]
            if 0 <= sz < h and 0 <= sy < n and 0 <= sx < m and tomato[sz][sy][sx] == 0:
                tomato[sz][sy][sx] = 1
                cnt += 1
                next_q.append([sz, sy, sx])
            
    del now_q
    return next_q, cnt

while queue:
    queue, cnt = bfs(queue, cnt)
    time+=1

print(time-1) if non+cnt==m*n*h else print(-1)

