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


    def show(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()
                


    def ll_sorted(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                temp2=self.start
                while temp2.next!=None:
                    if temp2.data>temp2.next.data:
                        temp2.data,temp2.next.data=temp2.next.data,temp2.data
                    temp2=temp2.next
                temp=temp.next
            self.show()


a=ll()
a.insert(23)
a.insert(45)
a.insert(12)
a.insert(1)
a.show()
a.ll_sorted()
