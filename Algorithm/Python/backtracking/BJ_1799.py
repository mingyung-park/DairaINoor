from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

count = [0,0]
max_num = [0,0]
left = [1 for _ in range(2*N)]
right = [1 for _ in range(2*N)]

def check(r,l,x,y):
    return board[y][x] and right[r] and left[l]

def dfs(r):
    if r>=2*N-1:
        max_num[r%2] = max(max_num[r%2], count[r%2])
        return
    
    start = abs(N-1-r)
    for l in range(start,2*N-1-start,2):

        y = (r+l-N+1)//2
        x = r-y

        if check(r,l,x,y):
            count[r%2] = count[r%2]+1
            board[y][x] = right[r] = left[l]=0
            dfs(r+2)
            board[y][x] = right[r] = left[l]=1 
            count[r%2] = count[r%2]-1 
            
        dfs(r+2)
            
    return

print(sum(max_num))