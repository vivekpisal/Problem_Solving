a=[[2],[3,4],[6,5,7],[4,1,8,3]]
minlen=0
val=0
for i in range(len(a)):
    if i==0:
        val=i
        minlen+=a[i][0]
    else:
        minval=min(a[i][val],a[i][val+1])
        minlen+=minval
        val=a[i].index(minval)

print(minlen)    
                
            
            
