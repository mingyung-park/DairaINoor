from collections import deque
from sys import stdin

N = int(stdin.readline())

col=[True for _ in range(N)]
right=[True for _ in range(2*N)]
left=[True for _ in range(2*N)]
count=[0]

def cannot_attack(x,y):
    return right[x+y] and left[N-y+x-1] and col[y]


def place_queen(n): #n번째 줄
    if n==N:
        count[0] = count[0]+1 #경우의 수 증가14
        return True # 탐색 완료
    
    for i in range(N):   
        if cannot_attack(n,i):
            right[n+i] = left[N-i+n-1] = col[i] = False
            place_queen(n+1)
            right[n+i] = left[N-i+n-1] = col[i] = True
        
    return False

place_queen(0)
print(count[0])