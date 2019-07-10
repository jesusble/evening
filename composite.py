n=int(input())
fact=0
for i in range(1,n):
  if n%i==0:
    fact=i
if fact>1:
  print ('yes')
else:
  print ('no')
