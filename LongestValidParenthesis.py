def valid(a,o=0,c=0,n=0):
    if n==len(a):
        if o>c:
            return c
        if c>o:
            return o
        if c==o:
            return True  
    if a[n]=="(":
        return valid(a,o+1,c,n+1)
    elif a[n]==")":
        return valid(a,o,c+1,n+1)
  




a="(()"
b=valid(a)
