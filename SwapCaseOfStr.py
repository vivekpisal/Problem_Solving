a="HacKerRanK"
a=list(a)
for i in range(len(a)):
    if a[i].isupper():
        a[i]=a[i].lower()
    elif a[i].islower():
        a[i]=a[i].upper()


print(''.join(a))
