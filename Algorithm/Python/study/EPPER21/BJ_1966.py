from sys import stdin
from collections import deque
import heapq

#큐의 가장 앞에 문서의 중요도 확인
#나머지 문서중 현재보다 중요도 높ㅍ다 -> 큐의 가장 마지막에 ㅇ재배피
# 아니면 바로 인쇄
def print_page(queue, target):
    cnt = 0
    for i, element in enumerate(queue):
        if i==target:
            queue[i] = [-element,True,i]
        else:
            queue[i] = [-element,False,i]
    heap = queue.copy()
    queue = deque(queue)
    
    heapq.heapify(heap)
    
    while queue:
        now = queue.popleft()
        if heap[0][0]==now[0]: # 현재 인쇄할것인 경우
            cnt = cnt+1
            heapq.heappop(heap)
            if now[1]:
                print(cnt)
                return
            heapq.heapify(heap)
        else:
            queue.append(now)
    
    return

tc = int(stdin.readline())
for _ in range(tc):
    N,M = map(int, stdin.readline().split())
    page_list = list(map(int, stdin.readline().split()))
    print_page(page_list, M)