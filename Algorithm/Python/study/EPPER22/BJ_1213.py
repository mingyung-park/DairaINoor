from sys import stdin
from collections import Counter, deque
name = list(stdin.readline().strip())
mid=[False]
def check_avail(name):
    counter = Counter(name)
    flag=True
    for val, cnt in counter.items():
        if cnt%2==0:
            continue
        
        if cnt%2==1 and flag:
            mid[0]=True
            flag=False
            mid.append(val)
            continue
        
        else:
            return False
    
    return True

def print_name(counter):
    if mid[0]:
        list=[key[0]*(key[1]//2) for key in counter]

        print(*list, sep='',end='')
        print(mid[1],end='')
        list.reverse()
        print(*list,sep='')
        
    else:
        list=[key[0]*(key[1]//2) for key in counter]

        print(*list, sep='',end='')
        list.reverse()
        print(*list,sep='')
        
counter = Counter(name)

if check_avail(name):
    if mid[0]:
        counter[mid[1]]=counter[mid[1]]-1
    counter = sorted(counter.items(), key= lambda pair: pair[0])
    print_name(counter)
else:
    print("I'm Sorry Hansoo")