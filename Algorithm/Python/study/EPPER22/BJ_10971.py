from sys import stdin
from collections import deque
INF = 1e8
#순회여행경로 계획. 가장 적은 비용. 
#아하 외판원 순회는 방문
N = int(stdin.readline())
cost = [list(map(int, stdin.readline().split())) for _ in range(N)]
travel_res=[0 for _ in range(N)]
ans = [INF]

def traveling(n, now, now_cost):

    if ans[0]<=now_cost: #의미 없는 탐색이므로 중지
        return 
    
    if n>=N: # 이동 제한
        if cost[now][0]!=0:
            ans[0] = min(ans[0], now_cost+cost[now][0])

        return
    
    for i in range(N):#시작 지점
        if travel_res[i]==0 and cost[now][i]!=0:
            travel_res[i]=1
            traveling(n+1,i,cost[now][i]+now_cost)
            travel_res[i]=0
    return 

travel_res[0]=1
traveling(1,0,0)
print(ans)