
def find(parent,node):
    if parent[node]!=node: 
        parent[node]=find(parent,parent[node])
        
    return parent[node]

def union(parent, node1, node2):
    root1 = find(parent,node1)
    root2 = find(parent,node2)
    
    if root1!=root2:
        if(root1<root2):
            parent[root2]=root1
        else:
            parent[root1]=root2

def kruskal(n, edges,parent):
    cost = 0
    cnt = 0
    for _, element in enumerate(edges):
        if cnt==n-1: 
            return cost
        
        if find(parent,element[0]) != find(parent,element[1]):
            union(parent,element[0],element[1])
            cost += element[2]
            cnt+=1
    return cost
    
from sys import stdin

input = stdin.readline
v,e = map(int,input().split())
parent =[i for i in range(v+1)]
edge =[]
for i in range(e):
    edge.append(list(map(int, input().split())))
edge.sort(key=lambda x: x[2])

print(kruskal(v,edge,parent))
