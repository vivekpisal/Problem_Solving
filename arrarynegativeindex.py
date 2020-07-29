a=[[-3,-2,-1,1],[-2,2,3,4],[4,5,7,8]]
c=0
for i in a:
    for j in i:
        if j<0:
            c+=1
print(c)



def func(M,n,m):
    count=0
    i=0
    j=m-1
    while j>=0 and i<n:
        if M[i][j]<0:
            count+=j+1
            i+=1
        else:
            j-=1

    return count

b=func(a,3,4)
