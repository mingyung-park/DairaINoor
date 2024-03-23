import sys
input = sys.stdin.readline().rstrip()
N = len(input)

idx = [-1 for _ in range(N)]
stack = []
now = 0

for i, c in enumerate(input):
    if c=='(':
        stack.append(i)
        idx[i]=now
        
    elif c==')':
        stack.pop()
        idx[i]=now
        now+=1

dict = [[] for _ in range(now)]
for i in range(now):
    for j in range(N):
        if(idx[i]==now):
            continue
        else:
            dict[i].append(input[j])