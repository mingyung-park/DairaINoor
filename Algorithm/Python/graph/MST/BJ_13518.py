from sys import stdin
import heapq
def prim(graph, start_node,reverse=True):
    total_cost = 0
    visited = set()
    
    min_heap = [(1,start_node)]

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue

        visited.add(node)
        if cost == 0:  total_cost+=1
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap,(w if not reverse else -w,neighbor))
                
    return total_cost

N, M = map(int,stdin.readline().split())

graph=[[] for _ in range(N+1)]
for i in range(M+1):
    A,B,C = map(int,stdin.readline().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
    
min_uphill = prim(graph, 0)
max_uphill = prim(graph, 0,reverse=False)


print(max_uphill**2-min_uphill**2)
