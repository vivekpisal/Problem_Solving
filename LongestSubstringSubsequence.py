a="pwkepsaw"
sbs=[]
c=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j] not in c:
            c.append(a[j])
        else:
            pass
        #print(j,end='')
    sbs.append(c)
    c=[]

print(''.join(sbs[0]))
