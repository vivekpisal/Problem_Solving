def search(a,l,r,ser):
    mid=(l+r)//2
    if a[mid]==ser:
        return True
    elif mid==l and l==r:
        return False
    elif a[mid]>ser:
        return search(a,l,mid-1,ser)
    elif a[mid]<ser:
        return search(a,mid+1,r,ser)


a=search([1,2,3,4,5,6,7,8],0,7,6)
