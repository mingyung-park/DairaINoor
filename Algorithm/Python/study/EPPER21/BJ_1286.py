from sys import stdin
from collections import deque

# 나무 판자는 크기 1, 양수의 길이
# -,|로 구분, -- -> 같은 판자
# 방 바닥은 세로N,가로M
# 나무 판자의 수

N, M =map(int, stdin.readline().split())
tiles =[stdin.readline().strip() for _ in range(N)]
tiles_t = list(zip(*tiles))
cnt = 0


for i in tiles:
    flag = True
    for j in i:
        if j=='-':
            if flag:
                cnt=cnt+1
            flag=False
        else:
            flag = True

flag = True
for i in tiles_t:
    flag = True
    for j in i:
        if j=='|':
            if flag:
                cnt=cnt+1
            flag=False
        else:
            flag = True
    
print(cnt)