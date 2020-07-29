#vowels
def kevin(s):
    word=[]
    v="AEIOU"
    for i in range(len(s)):
        if s[i] in v:
            for j in range(i,len(s)):
                if s[i:j+1] not in word:
                    word.append(s[i:j+1])
    return word


#consonants
def staurt(s):
    v="AEIOU"
    word=[]
    for i in range(len(s)):
        if s[i] not in v:
            for j in range(i,len(s)):
                if s[i:j+1] not in word:
                    word.append(s[i:j+1])
    return word


s="BANANA"
wo=kevin(s)
wo1=staurt(s)

