import math
xh,yj=map(int,input().split())
c=xh*yj
a=math.sqrt(c)
if(c==(a*a)):
  print('yes')
else:
  print('no')
