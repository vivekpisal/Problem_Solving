def merge(num,num1):
    i=0
    j=0
    c=[]
    while i<len(num) and j<len(num1):
        if num[i]<num1[j]:
            c.append(num[i])
            i+=1
        elif num[i]>num1[j]:
            c.append(num1[j])
            j+=1
    if i<len(num1):
        while i<len(num):
            c.append(num[i])
            i+=1
    elif j<len(num1):
        while j<len(num1):
            c.append(num1[j])
            j+=1
    return c
    



a=[1,3,5,7,9]
b=[2,4,6,8,10]
ans=merge(a,b)
