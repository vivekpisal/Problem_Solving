'''a=[-1,0,1,2,-1,-4]
sum=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        for k in range(j,len(a)):
            if a[i]==0 and a[j]==0 and a[k]==0:
                continue
            if a[i]+a[j]+a[k]==0:
                sum.append(sorted([a[i],a[j],a[k]]))

sum1=[]
f=False
for i in range(len(sum)):
    for j in range(i+1,len(sum)):
        if sum[i]==sum[j]:
            f=True
            break
        else:
            f=False
            pass
    if f==False:        
        sum1.append(sum[i])


print(sum1)'''

class Enum:
    tim ,joe ,vaivi=range(1,4)


print(Enum.vaivi)
