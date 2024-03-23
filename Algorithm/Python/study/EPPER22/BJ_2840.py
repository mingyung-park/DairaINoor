from sys import stdin
from collections import Counter


n,k = map(int, stdin.readline().split())
info = [list(stdin.readline().split()) for _ in range(k)]
now = [0]
ans = ['?']*n

def get_alphabet(info_):
    now[0] = (now[0]+int(info_[0]))%n
    if ans[now[0]]=='?':
        ans[now[0]]=info_[1]
    elif ans[now[0]]!=info_[1]:
        return False
    return True

def check_valid():
    counter = Counter(ans)
    for char, count in counter.items():
        if char =='?':
            continue
        if count >=2:
            return False
        
    for i in range(n):
        if (ans[i] == ans[(i+1)%n]) and ans[i]!='?':
            return False
    
    return True
    
def print_ans(ans):
    if check_valid():
        for i in range(n):
            print(ans[(now[0]-i)%n],end='')
        return
    print('!')
    return
    
        
for i in range(k):
    if not get_alphabet(info[i]):
        print('!')
        break
    if i==k-1:
        print_ans(ans)
