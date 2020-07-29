def merge(l,r,mid,a):
    d=mid+1
    f=[]
    print(l,r,mid,a)
    while l<=mid and d<=r:
        if a[l]<a[d]:
            f.append(a[l])
            l+=1
        elif a[l]>a[d]:
            f.append(a[d])
            d+=1
    return f
        




def mergesort(l,r,a):
    if l<r:
        mid=(l+r)//2
        mergesort(l,mid,a)
        mergesort(mid+1,r,a)
        f=merge(l,r,mid,a)
        return f


a=[10,9,8,7,6,5,4,3]
f=mergesort(0,len(a)-1,a)
