class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class scl:
    def __init__(self):
        self.start=None

    def insert(self,value):
        newnode=node(value)
        if self.start==None:
            self.start=newnode
            newnode.next=self.start

        else:
            t=self.start
            while t.next!=self.start:
                t=t.next
            t.next=newnode
            newnode.next=self.start


    def show(self):
        if self.start==None:
            print('list is empty')
        else:
            t=self.start
            while t.next!=self.start:
                print(t.data,end=' ')
                t=t.next
            print(t.data)

a=scl()
a.insert(23)
a.insert(34)
a.insert(45)
a.insert(56)
a.show()
