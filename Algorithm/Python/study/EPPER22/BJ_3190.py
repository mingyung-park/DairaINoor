from sys import stdin
from collections import deque

# 사과 먹으면 늘어남
#자기자신과 충돌시 게임오버
#NN 정사각 보드
# 이동칸에 사과 있으면 사과가 없어지고, 꼬리가 움직이지 않음. 이동칸에 없으면 꼬리는 비움

N = int(stdin.readline())
K = int(stdin.readline())
apple = [list(map(int,stdin.readline().split())) for _ in range(K)]
L = int(stdin.readline())
snake_info= [list(stdin.readline().split()) for _ in range(L)]

snake_body = deque([[0,0]])
move_x= [1,0,-1,0]
move_y= [0,1,0,-1]


def snake_move():
    move_idx = 0
    t = 0
    while True:
        t=t+1
        target = [snake_body[-1][0]+move_x[move_idx],snake_body[-1][1]+move_y[move_idx]]

        snake_body.append(target)# 머리 이동
        #
        # 머리가 벽에 부딛히거나, 몸에 부딛히는지 검사
        if not (0<=target[0]<N and 0<=target[1]<N and (snake_body.count(target)==1)):
            print(t)
            return # 종료            
        
        #
        #꼬리 계산
        if [target[1]+1,target[0]+1] in apple:  
            apple.remove([target[1]+1,target[0]+1])
        else:
            snake_body.popleft()

        
        # 다음 단계의 rotation확인한다.    
        if snake_info and snake_info[0][0]==str(t):
            #rotate
            if snake_info[0][1]=='D':
                move_idx=(move_idx+1)%4

            else:
                move_idx=(move_idx-1)%4

            snake_info.pop(0)

snake_move()

