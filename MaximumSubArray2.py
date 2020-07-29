a=[-2,1,-3,4,-1,2,1,-5,4]
sum1=0
s=[0]
nums=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        sum1=sum1+a[j]
        if sum1>max(s):
            nums.append(a[i:j+1])
            s.append(sum1)
    sum1=0


print(max(nums))
print(max(s))
            
