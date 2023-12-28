from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # Skip if the current distance is greater than the stored distance
        if distance[now] < dist:
            continue

        # Explore neighbors of the current node
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# V == 5일 때 1~5까지 노드가 있는 것입니다.
V, E = map(int, input().split())

snode = int(input())  # 시작 노드

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)  # 최단 거리 테이블

# 연결 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(snode)

# i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
