a=[[1,2],[2,6],[8,10],[11,18],[18,34]]
for i in range(len(a)-2):
    if a[i][1]==a[i+1][0]:
        a[i][1]=a[i+1][1]
        a.pop(i+1)
        
