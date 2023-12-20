from sys import stdin
from collections import deque
tomato=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
rotten=deque()
empty = 0
time=0
cnt = 0

m,n = map(int,stdin.readline().split())
for i in range(n):
    temp=list(map(int,stdin.readline().split()))
    tomato.append(temp)
    for j in range(m):
        if(temp[j]==1):
            rotten.append((i,j))
        elif(temp[j]==-1):
            empty+=1


def bfs(rotten):
    check=0
    next_rotten = deque()
    while rotten:
        x, y = rotten.popleft()
        for i in range(4):
            target_x = x+dx[i]
            target_y = y+dy[i]
            if 0 <= target_x < n and 0 <= target_y < m and tomato[target_x][target_y]==0 :
                next_rotten.append((target_x,target_y))
                tomato[target_x][target_y]=1
                check+=1

    return check, next_rotten


while rotten:
    count, rotten = bfs(rotten)
    if count != 0:
        time += 1

for i in range(n):
    cnt += tomato[i].count(1)

if n * m - empty == cnt:
    print(time)
else:
    print(-1)