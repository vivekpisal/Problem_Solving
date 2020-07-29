a=["flower","flow","flight"]
k=0
c=[]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j][k]==a[j+1][k]:
            f=True
        else:
            f=False
            break
    if f==True:
        c.append(a[j][k])
    k+=1
print(*c)
k=0
c.clear()
for i in range(len(a)):
    for j in range(1,len(a)):
        ch=a[0][:k+1]
        if ch in a[j]:
            f=True
        else:
            f=False
    if f:
        c.append(ch)
    k+=1

print(c[-1])
    

