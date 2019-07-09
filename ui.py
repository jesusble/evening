ab1 = input()
ab2 = input()
de_string = ''
l = []
for i in range(26):
    l.append(chr(i+97))

for i in range(len(ab2)):
    ab2_pos = l.index(ab2[i]) + 1
    ab1_pos = l.index(ab1[i]) + 1
    if ab1_pos + ab2_pos > 26:
        pos = ab1_pos - (26 - ab2_pos)
        de_string += l[pos-1]
    else:
        pos = ab1_pos + ab2_pos
        de_string += l[pos-1]
print(de_string)
