n=int(input())

list = []
for i in range(n):
    [a,b]=map(int,input().split())
    list.append([a,b])
list.sort()
sortedL=sorted(list,key = lambda x: (x[1],x[0]))
for i, row in enumerate(list):
    print(row[0],row[1])