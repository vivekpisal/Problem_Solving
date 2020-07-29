class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.start=None


    def insert(self,value):
        newnode=node(value)
        if self.start==None:
            self.start=newnode
            newnode.next=self.start

        else:
            t=self.start
            self.start=newnode
            newnode.next=t
            f=t
            while f.next!=t:
                f=f.next
            f.next=self.start
           


    def show(self):
        if self.start==None:
            print('List is empty')
        else:
            t=self.start
            while t.next!=self.start:
                print(t.data)
                t=t.next
            print(t.data)


a=ll()
a.insert(35)
a.insert(25)
a.insert(5)
a.insert(23)
a.insert(gh3)

a.show()
