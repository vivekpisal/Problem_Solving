a=["flower","flowxx","flowf"]
k=0
c=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[j][i]==a[0][k]:
            f=True
        else:
            f=False
            break
    if f==True:
        c.append(a[i][k])
        k+=1
    else:
        break
        
    
        
