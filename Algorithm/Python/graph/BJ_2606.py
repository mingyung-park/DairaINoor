def find(a,parent):
    while parent[a]!=a:
        a=parent[a]
    return a

def union(a,b,parent):
    p1 = find(a,parent)
    p2 = find(b,parent)
    if not p1==p2:
        if p1<p2:
            parent[p2]=p1
        else:
            parent[p1]=p2


computer=int(input())
parent = [i for i in range(computer+1)]

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    union(a,b,parent)

cnt=0
target=find(1,parent)
for i in range(2,computer+1):
    if find(i,parent)==target:
        cnt+=1
print(cnt)