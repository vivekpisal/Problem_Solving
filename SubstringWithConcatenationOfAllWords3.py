s="barfoothefoobarman"
words=["foo","bar"]
w=words[0]+words[1]
wa=words[1]+words[0]
p=[]
for i in range(len(s)):
    if w[0]==s[i] or wa[0]==s[i]:
        k=i
        l=0
        for j in range(i,i+len(w)):
            if w[l]==s[j] or wa[l]==s[j]: 
                f=True
            else:
                f=False
                break
            l+=1
        if f:
            p.append(k)
            
    
