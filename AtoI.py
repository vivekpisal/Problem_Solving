def AtoI(str):
    st=[]
    for i in str:
        if i==' ':
            pass
        elif (i=='-' or i=='+') or (i>='1' and i<='9'):
            st.append(i)
        else:
            break
    return st

a=AtoI("-4193")
j=0
sum=0
for i in range(len(a)-1,-1,-1):
    if a[i]=='-':
        sum=-sum
    else:
        sum=sum+int(a[i])*(10**j)
        j+=1
    
print(sum)
