n=int(input())
k=list(map(int,input().split()))
cnt=n
for i in k:
    if(i==1):
        cnt=cnt-1
        continue
    for j in range(2,i):
        if(i%j==0): 
            cnt=cnt-1
            break

print(cnt)            
            
   