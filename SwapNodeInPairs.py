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
            print('List is empty')
        else:
            temp=self.start
            while temp.next!=None:
                print(f'{temp.data}',end='->')
                temp=temp.next
            print(temp.data)


    def pair(self):
        temp=self.start
        temp1=self.start
        while temp1.next!=None:
            temp,temp.next=temp.next,temp
            temp1=temp1.next
            

    

a=ll()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.show()
a.pair()
a.show()
