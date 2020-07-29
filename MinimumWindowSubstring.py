s="ADOBECODEBANC"
t="ABC"
c=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        if t[0] in s[i:j+1] and t[1] in s[i:j+1] and t[2] in s[i:j+1]:
            c.append([len(s[i:j+1]),s[i:j+1]])

print(min(c)[1])



        
