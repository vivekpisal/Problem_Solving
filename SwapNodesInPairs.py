class  node:
    def __init__(self,data):
        self.data=data
        self.next=None


class ll:
    def __init__(self):
        self.start=None

    def insert(self,value):
        if self.start is None:
            self.start=node(value)

        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=node(value)


    def view(self):
        if self.start is None:
            print('List is empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            print()



a=ll()
a.insert(23)
a.insert(45)
a.insert(56)


        
            
