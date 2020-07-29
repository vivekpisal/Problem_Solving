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
            newnode=node(data)
            temp=self.start.next
            self.start.next=newnode
            newnode.next=temp


    def show(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next

a=ll()
a.insert(10)
a.show()
            
