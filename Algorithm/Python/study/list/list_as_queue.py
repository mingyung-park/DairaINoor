# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Using list as Stacks
# Queue : First In First Out, 먼저 들어간 것이 먼저 나온다.

# Queue를 list로 구현하는 것은 효율적인 방법은 아니다. 
# append를 이용해서 뒤에 넣고, pop(0)를 이용해서 빼는 경우에 모든 element의 이동이 발생하기 때문
queue = []
queue.append('a')
queue.append('b')
print(queue)

queue.pop(0)
print(queue)
 
# 따라서 append와 pop을 빠르게 수행할 수 있는 collections.deque를 사용하여 구현한다.
from collections import deque

queue = deque([])
queue.append('a')
queue.append('b')
print(queue)
#queue.popleft()
queue.pop()
print(queue)
