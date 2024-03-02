from sys import stdin
from collections import deque


sudoku = [list(map(int,  stdin.readline().split())) for _ in range(9)]
target = deque((i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0)


def is_valid(x,y,num):
    row = sudoku[x]
    column = [sudoku[i][y] for i in range(9)]
    box = [sudoku[i][j] for i in range(3 * (x // 3), 3 * (x // 3) + 3) for j in range(3 * (y // 3), 3 * (y // 3) + 3)]
    return num not in set(row) and num not in set(column) and num not in set(box)

def get_possible_values(x, y):
    used_numbers = set(sudoku[x] + [sudoku[i][y] for i in range(9)] +
                      [sudoku[i][j] for i in range(3 * (x // 3), 3 * (x // 3) + 3) for j in range(3 * (y // 3), 3 * (y // 3) + 3)])
    return [num for num in range(1, 10) if num not in used_numbers]

def DFS():
    if not target:
        for row in sudoku:
            print(*row) 
        return True #solve

    now_x, now_y = target.popleft()
    possible_values = get_possible_values(now_x, now_y)
    
    for num in possible_values:
        sudoku[now_x][now_y] = num
        target.remove((now_x, now_y))
        if DFS():
            return True #solve
        sudoku[now_x][now_y] = 0
        target.appendleft((now_x, now_y))

    return False   


DFS()