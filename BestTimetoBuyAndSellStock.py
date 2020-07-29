a=[7,1,5,3,6,4]
c=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        c.append(a[j]-a[i])

if max(c)>0:
    print(max(c))
else:
    print(0)

