
def binary_search(list, target):
    # left: 탐색 대상의 처음 인덱스
    # right: 탐색 대상의 마지막 인덱스
    
    left = 0,
    right = len(list)-1
    
    while left<right:
        mid = (left+right)/2
        if list[mid]>target:
            right = mid-1
        elif list[mid]<target:
            left = mid+1
    
    return (left+right)/2