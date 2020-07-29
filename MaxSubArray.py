a=[1,-3,2,1,-1]
sum=0
m=[]
c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if i+1==j:
            sum=a[i]+a[j]
            print(sum)
        else:
            if sum<sum+a[j]:
                sum=sum+a[j]
                print(f"*{sum}")

    m.append(sum)
    sum=0
    print(m)
        
