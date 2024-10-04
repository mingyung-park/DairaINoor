#BOJ_9019번 DSLR
from sys import stdin

from collections import deque
def D(n):
    return (n*2)%10000
def S(n):
    return (n-1)%10000
def L(n):
    return (n%1000)*10 + n//1000
def R(n):
    return (n//10)+(n%10)*1000

def bfs(A, B):
    queue = deque([(A, "")]) 
    visited = [False] * 10000
    visited[A] = True
    
    # BFS 탐색 시작
    while queue:
        current, path = queue.popleft()
        
        # 목표 값에 도달하면 명령어 경로 반환
        if current == B:
            return path
        
        # 다음 명령어로 상태를 변경하고 큐에 삽입
        for command, next_num in [("D", D(current)), ("S", S(current)), ("L", L(current)), ("R", R(current))]:
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, path + command))
    
    return ""

def solution():
    T= int(stdin.readline())
    ans=[]
    for _ in range(T):
        A, B=map(int, stdin.readline().split())
        ans.append(bfs(A,B))
    return ans

print("\n".join(solution()))

T= int(stdin.readline())
for i in range(T):
    print(solution())




import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T):
    ch = [False for _ in range(10001)]
    A, B = map(int, sys.stdin.readline().strip().split())
    
    Q = deque()
    Q.append([A, ''])
    ch[A] = True

    while Q:
        n, cmd = Q.popleft()
        
        # B(최종 값)과 A에 연산을 적용한 n과 동일하다면
        if n == B:
        # 적용한 연산들 출력 후 while문 종료
            print(cmd)
            break

        # D
        d = (n * 2) % 10000
        if not ch[d]:
            ch[d] = True
            Q.append([d, cmd + 'D'])

        # S
        s = (n - 1) % 10000
        if not ch[s]:
            ch[s] = True
            Q.append([s, cmd + 'S'])

        # L
        l = n//1000 + (n % 1000) * 10
        if not ch[l]:
            ch[l] = True
            Q.append([l, cmd + 'L'])

        # R
        r = n//10 + (n%10) * 1000
        if not ch[r]:
            ch[r] = True
            Q.append([r, cmd + 'R'])