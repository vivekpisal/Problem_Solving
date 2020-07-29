a="Www.HacKerRank.Com"
s=""
for i in range(len(a)):
    if not a[i].isalnum():
        s=s+a[i]
    elif(a[i].islower()):
        s=s+a[i].upper()
    elif(a[i].isupper()):
        s=s+a[i].lower()
    else:
        s=s+a[i]
        
