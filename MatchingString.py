a="welcome"
b="wel"
c=[]

f=False
for i in range(len(a)):
    if b[0]==a[i]:
        k=i
        for j in range(0,len(b)):
            if b[j]==a[k]:
                f=True
                c.append(a[k])
                k+=1
            else:
                f=False
                break
    if f:
        break

if f:
    print(f"Found")
else:
    print("Not found")


'''
i=0
while(i<len(b)-1):
    j=0
    while(j<len(a)-1):
        if(a[j]==b[i]):
            c.append(b[i])
            i+=1
            j+=1
            f=True
        else:
            f=False
            i+=1

    if(f==True and i==len(a)-1):
        break
    if(f==False):
        break'''
