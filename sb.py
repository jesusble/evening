sb1,r1=list(map(int,input().split()))
sb2,r2=list(map(int,input().split()))  
sb3,r3=list(map(int,input().split()))  
sb4,r4=list(map(int,input().split())) 
a=r2-r1
b=r3-r4
c=sb3-sb2
d=sb4=sb1
if(a==b==c==d):
  print("yes")
else:
  print("no")
