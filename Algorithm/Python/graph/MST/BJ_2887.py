#BOJ2887 행성터널
from sys import stdin
N = int(stdin.readline())

nodes = [(*map(int, stdin.readline().split()), i) for i in range(N)]
#kruskal algorithm

def find(node, parent):
    if node==parent[node]:
        return node
    node = find(parent[node],parent) 
    return node

def union(node1, node2, parent):
    root1 = find(node1,parent)
    root2 = find(node2,parent)
    if root1>root2:
        parent[root1]=root2
    elif root2>root1:
        parent[root2]=root1 


def kruskal(edges,parent):   
    cnt=0
    cost = 0
    for i in range(N*3-3):
        if cnt==N-1:
            return cost
        if find(edges[i][0],parent)==find(edges[i][1],parent):
            continue
        else:
            union(edges[i][0],edges[i][1],parent)
            cost+=edges[i][2]
            cnt+=1
    return cost

    

edges = []
node_x = sorted(nodes, key=lambda x: x[0])
for i in range(N-1):
    cost = abs(node_x[i][0]-node_x[i+1][0])
    edges.append([node_x[i][3],node_x[i+1][3],cost])
    
node_y = sorted(nodes, key=lambda x: x[1])
for i in range(N-1):
    cost = abs(node_y[i][1]-node_y[i+1][1])
    edges.append([node_y[i][3],node_y[i+1][3],cost])
    
node_z = sorted(nodes, key=lambda x: x[2])
for i in range(N-1):
    cost = abs(node_z[i][2]-node_z[i+1][2])
    edges.append([node_z[i][3],node_z[i+1][3],cost])

edges.sort(key=lambda x : x[2])
parent = [i for i in range(N)]

print(kruskal(edges,parent))
