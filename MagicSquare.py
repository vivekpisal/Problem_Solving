a=[[3,3,3],
   [3,3,3],
   [3,3,3]]
for i in a:
    print(i)

sumr=[]
sum=0
sum1=0
for i in a:
    for j in i:
        sum=sum+j

    sumr.append(sum)
    sum=0

sumc=[]
sumc1=0
sumc2=0
sumc3=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if j==0:
            sumc1=sumc1+a[i][j]
        if j==1:
            sumc2=sumc2+a[i][j]
        if j==2:
            sumc3=sumc3+a[i][j]
sumc.append(sumc1)
sumc.append(sumc2)
sumc.append(sumc3)

sumd=0
for i in range(len(a)):
    sumd=sumd+a[i][i]
sumdr=0
for  i in range(len(a)-1,-1,-1):
    sumdr=sumdr+a[i][i]


if sumc==sumr:
    if sumd==sumdr:
        print("magic square")
    else:
        print("not magic square")
else:
    print("not magic sqaure")


