import sys
input=sys.stdin.readline

word = list(map(int,input().rstrip()))
l = len(word)
dp=[1,1]+[0]*l
print(word)
if word[0]==0:
    print(0)
else:
    for i in range(1,l):
        print(word[i])
        j=i+1
        if word[i]>0:
            dp[j]+=dp[j-1]
        if 10<=word[i]+word[i-1]*10<=26:
            dp[j]+=dp[j-2]
    print(dp[l]%1000000)
