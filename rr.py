sb=int(input())
aj=list(map(int,input().split()))
for p in range(len(aj)-1):
     if(aj[p]>aj[p+1]):
           print(p)
           break
