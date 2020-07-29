a=[]
def enqueue(no):
    a.append(no)
    print(a)



def dequeue():
    if a==[]:
        print('Queue is empty')
    else:
        a.pop(0)
        print(a)

    

while True:
    i=int(input('choose'))
    if i==1:
        no=int(input('enter the value'))
        enqueue(no)
    elif i==2:
        dequeue()
    elif i==3:
        break
