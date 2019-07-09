sb=input()
flagg=0
for i in range(0,len(sb)-1):
  for j in range(i+1,len(sb)):
    if sb[i]<sb[j]:
      flagg=1
      print(sb[j:])
      break
  if flagg==1:
    break
else:
  print(sb)
	
	
