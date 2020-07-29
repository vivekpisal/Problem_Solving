class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class ll:
    def __init__(self):
        self.start=None

    def insert(self,data):
        if self.start==None:
            self.start=node(data)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)

    def view(self):
        if self.start==None:
            print('List is empty')
        else:
            temp=self.start
            print()
            while temp.next!=None:
                print(temp.data,end='->')
                temp=temp.next
            print(temp.data)


a=ll()
while True:
    i=int(input('choose 1:Insert 2:View 3:Break'))
    if i==1:
        val=int(input('enter the value in the LL'))
        a.insert(val)
    elif i==2:
        a.view()
    elif i==3:
        break
    else:
        print('Wrong Choice')
