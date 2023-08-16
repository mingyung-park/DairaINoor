# 2751 수 정렬하기2
import sys

input = sys.stdin.readline()
n = int(input())
num=[]
for i in range(n):
    num.append(int(input)) 
num.sort()
for i in num:
    print(i)
