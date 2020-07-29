s="ADOBECODEBANC"
t="ABC"
info=[]
for i in range(len(s)):
    for j in range(len(s)):
        if t[0] in s[i:j+1] and t[1] in s[i:j+1] and t[2] in s[i:j+1]:
            info.append([len(s[i:j+1]),s[i:j+1]])

print(min(info))
            
        
