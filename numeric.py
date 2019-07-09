s=input()
sb=[]
for i in s:
	if i.isnumeric():
		sb.append(i)
print(''.join(sb))
