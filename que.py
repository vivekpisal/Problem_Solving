a=[]
def dequeue():
    if a==[]:
        print('Queue is empty')
    else:
        a.pop(0)

def enqueue(val):
    a.append(val)


while True:
    i=int(input('1:enq  2:deq 3:break'))
    if i==1:
        val=int(input('enter the element'))
        enqueue(val)
    elif i==2:
        dequeue()
    elif i==3:
        break
