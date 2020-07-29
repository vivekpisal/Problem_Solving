a="vaishnavi ghadge"
w=[]
k=0
for i in range(len(a)):
    if i==0:
        w.append(a[0].upper())

    elif a[i]==' ':
        w.append(a[i+1].upper())
        k=i+1

    else:
        if k==i:
            continue
        else:
            w.append(a[i])

print(*w)
