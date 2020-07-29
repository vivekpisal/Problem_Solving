a=[-2,1,-3,4,-1,2,1,-5,4]
sum1=0
s=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        sum1=sum1+a[j]
        if sum1>sum(s):
            s.append(sum1)
            sum1=0


print(max(s))
