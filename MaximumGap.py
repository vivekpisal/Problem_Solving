a=[3,6,9,1]
i=len(a)-1
while i>=0:
    j=len(a)-1
    while a[j]<a[j-1] and j>0:
        a[j],a[j-1]=a[j-1],a[j]
        j-=1
    i-=1

count=[]
for i in range(len(a)):
    for j in range(len(a)):
        count.append(a[j]-a[j-1])

print(max(count))