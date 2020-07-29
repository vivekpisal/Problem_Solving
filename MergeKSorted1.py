class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.start=None

    def insert(self,val):
        if self.start==None:
            self.start=node(val)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=node(val)

    def view(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp.next!=None:
                print(temp.data,end='->')
                temp=temp.next
            print(temp.data)

    def merge(self,a=None):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            for i in a:
                while temp.next!=None:
                    temp=temp.next
                temp.next=i.start
                temp=self.start
            self.view()

a=LL()
a.insert(23)
a.insert(34)
a.insert(45)
a.insert(56)
a.view()
b=LL()
b.insert(5)
b.insert(65)
b.insert(12)
c=LL()
c.insert(22)
a.merge([b,c])
