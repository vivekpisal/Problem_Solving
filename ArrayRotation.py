a=[1,2,3,4,5]
j=4

for i in range(len(a)):
    if i+j>=len(a):
        k=len(a)-i
        f=j-k
        a[0+f]=a[i]
    else: 
        f=i+j
        a[f]=a[i]
      
print(a)