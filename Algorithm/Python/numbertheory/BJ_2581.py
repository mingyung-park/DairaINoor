m=int(input())
n=int(input())
list=[1 for i in range(n+1)]
list[0] = 0
list[1] = 0

for i in range(2,n+1):
    for j in range(i):
        if(list[j] and i%j==0):
            list[i]=0
            break
sum_prime=sum([j for j in range(m, n + 1) if list[j] == 1])
if sum_prime==0:
    print(-1)
else:
    print(sum_prime)
    print(list[m:n+1].index(1)+m)
