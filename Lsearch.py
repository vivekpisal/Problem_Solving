a=[23,45,22,67,89,3,44]
ser=int(input('enter the search element'))
f=1
for i in a:
    if ser in a:
        f=0
        break
    else:
        f=1

if f==0:
    print('element is found')
else:
    print("not found")

