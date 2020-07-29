def median(a):
    median=[]
    for i in range(len(a)):
        if len(a[i])%2==0:
            m=len(a[i])//2
            med=a[i][m]+a[i][m-1]
            median.append(med/2)
        else:
            m=len(a[i])//2
            median.append(a[i][m])

    return sum(median)/2
        

a=median([[1,2],[3,4]])
