class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dcll:
    def __init__(self):
        self.tail=None
        self.start=None


    def insert(self,value):
        newnode=node(value)
        if self.start==None:
            self.start,self.tail=newnode,newnode
            newnode.prev=self.start
            newnode.next=self.start
        else:
            t=self.start
            while t.next!=self.start:
                t=t.next
            t.next,self.tail=newnode,newnode
            newnode.prev=t
            newnode.next=self.start



    def show(self):
        if self.start==None:
            print('List is empty')
        else:
            t=self.start
            while t.next!=self.start:
                print(t.data)
                t=t.next
            print(t.data)



    def delete(self):
        if self.start==None:
            print('list is empty')
        else:
            self.tail.prev.next=self.start
        


a=dcll()
a.insert(12)
a.insert(23)
a.insert(34)
a.insert(45)
a.show()
