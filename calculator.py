while True:
    a=int(input('1st value'))
    b=int(input('2nd value'))
    op=int(input('1:add 2:sub 3:div 4:mul 5:break'))
    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a//b)
    elif op==4:
        print(a*b)
    elif op==5:
        break
