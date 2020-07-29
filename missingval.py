a=[3,4,-1,1,2]
c=[]
b=max(a)
for i in range(1,b+2):
    if i in a:
        pass
    else:
        c.append(i)

print(min(c))
