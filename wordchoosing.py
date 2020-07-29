  
print("\t\t\t-------------Word Chossing app---------------")
b=[i for i in "computer"]
a=[i for i in "c*mp*te*"]

for i in range(len(a)):
    if(a[i]==b[i]):
        continue
    else:
        print(*a)
        c=input("choose the letter:")
        if(b[i]==c):
            a[i]=c
        else:
            c=input('you have 1 more chance to choose this letter:')
            if(c==b[i]):
                a[i]=c
for i in a:
    if i=='*':
        print('you are unable to guess the word')
        break
else:
    print('you have succesfully guess the word')
print(*a)
