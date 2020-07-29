a="aab"
ans=[]
for i in range(len(a)):
    for j in range(len(a)):
        temp=[]
        while i!=j and j>0 and i<j:
            if a[i]==a[j]:
                temp.append(a[i])
                i+=1
                j-=1
            else:
                break
        else:
            temp.append(a[i])
        if temp not in ans:
            ans.append(temp)
ans=set(ans)
print(ans)
    
