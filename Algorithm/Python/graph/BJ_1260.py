from collections import deque
def bfs(graph,start):
    visited=[True]+[False for _ in range(n)]
    queue =deque([start])
    while(queue):
        now = queue.popleft()
        if(not visited[now]):
            visited[now]=True
            print(f"{now}", end=" ")
            queue.extend(map(int,graph[now][1:]))

def dfs(graph,start):
    visited=[True]+[False for _ in range(n)]
    stack = deque([start])
    while(stack):
        now=stack.pop()
        if not visited[now]:
            visited[now]=True
            print(f"{now}",end=" ")
            stack.extend(reversed(list((map(int, graph[now][1:])))))


from sys import stdin
n,m,v= map(int,stdin.readline().split())
node=[[0] for i in range(n+1)]
for i in range(m):
    s,e=map(int,stdin.readline().split())
    node[s].append(e)
    node[e].append(s)

for i in range(m):
    node[i].sort()

dfs(node,v)
print()
bfs(node,v)
