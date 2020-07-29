a="racecar"
r=len(a)-1
l=0
while r>=0 and l<len(a) and a[r]==a[l]:
    r-=1
    l+=1

r+=1
b=a[r:l]
if a==b:
    print('palindrome')
else:
    print('not palindrome')

