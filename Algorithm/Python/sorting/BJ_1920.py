n=int(input())
a = list(map(int,input().split()))
m=int(input())
b = list(map(int,input().split()))
a.sort()

def binary_search(list, target):
    low, high = 0, len(list)-1
    while low<=high:
        mid = (low+high)//2
        mid_value = list[mid]
        if(mid_value==target):
            return 1
        elif mid_value>target:
            high = mid-1
        elif mid_value<target:
            low = mid+1
        
    return 0

for i in b:
    print(binary_search(a,i))