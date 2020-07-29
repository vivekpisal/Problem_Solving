a=[5,6,100,4,200,1,3,2]
b=[]
for i in range(len(a)):
    if a[i]+1 in a or a[i]-1 in a:
        b.append(a[i])

print(sorted(b))
