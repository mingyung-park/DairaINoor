from sys import stdin
from collections import deque

# 쇠 막대기 사이에 레이저가 n개 존재하면 하나의 쇠막대기는 n+1개로 나뉜다.
# 괄호가 스텍에 들어가고, 다음 단계에 나와 pop 되는 순간이 레이저 발사순간.
# 그때 남아있는 괄호의 수 = 잘리는 막대기 수 -> +괄호 수 만큼 막대기 증가
# 처음 ( 들어가고 다음 단계에 pop 안되면 현재 막대기 수에 추가.(새로운 막대기)

sticks=0
stack = deque()
brackets = list(stdin.readline().strip())

def check_laser(now_idx):
    if brackets[now_idx-1]=='(':
        return True
    return False    

for i, element in enumerate(brackets):
    if element=='(':
        stack.append('(')
    else:
        if check_laser(i):
            stack.pop()
            sticks=sticks+len(stack)
        else:
            stack.pop()
            sticks=sticks+1

print(sticks)