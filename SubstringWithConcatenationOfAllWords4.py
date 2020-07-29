s="barfoothefoobarman"
a=["foo","bar"]
word=a[0]+a[1]
for i in range(len(s)):
    if word[0]==s[i]:
        k=0
        for j in range(i,i+len(word)):
            if word[k]==s[j]:
                f=True
                k+=1
            else:
                f=False
                break
        if f==True:
            print('Found')
