a=9
ans=[]
while a!=0:
    r=a%2
    a=a//2
    ans.append(r)
    
x=ans[:]
print(*ans)


d=10
ans1=[]
while d!=0:
    r=d%2
    d=d//2
    ans1.append(r)
y=ans1[:]
ans1.reverse()
print(*ans1)


c=0
add=[]
for i in range(len(x)-1,-1,-1):
    if x[i]==0 and y[i]==0:
        if c==1:
            add.append(1)
            c=0
        else:
            add.append(0)
            c=0
    elif x[i]==1 and y[i]==1:
        if c==1:
            add.append(1)
            c=1
        else:
            add.append(0)
            c=1
    elif (x[i]==1 and y[i]==0) or (x[i]==0 and y[i]==1):
        if c==1:
            add.append(0)
            c=1
        else:
            add.append(1)
            c=0
        
add.reverse()
print(add)
