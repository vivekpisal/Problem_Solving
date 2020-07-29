a=[[5,9],[1,2],[3,4],[0,6],[5,7],[8,9]]
print(a)
b=[]
a.sort()
print(a)
if a[0][0]==0:
    a.remove(a[0])
    b.append(a[0])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i][1]<=a[i+1][0]:
            b.append(a[i+1])
            break
        else:
            a.remove(a[i+1])
            
print(*b)
