aj=input()
sb=''
li=[]
for i in aj:
    if i not in li:
        sb+=i
        li.append(i)
    elif i in li:
        break
print(len(li))
