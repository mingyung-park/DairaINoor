from sys import stdin
import heapq
n = int(stdin.readline())
lec_time = [list(map(int, stdin.readline().split())) for  _ in range(n)]

lecture = [-1]


def get_min():
    lec_time.sort()
    
    for time in lec_time:#하나씩 합칠 수 있는 강의는 합친다(강의실)
        if lecture[0]<=time[0]:#lecture는 정렬된 최소 힙으로,
            heapq.heappop(lecture)
        heapq.heappush(lecture,time[1])
        
    return len(lecture)

print(get_min())

