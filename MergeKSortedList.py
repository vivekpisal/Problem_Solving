class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class ll:
    def __init__(self):
        self.start=None


    def insert(self,value):
        if self.start==None:
            self.start=node(value)

        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(value)


    def show(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()



    def merge(self,a):
        temp=self.start
        for i in range(len(a)):
            while(temp.next!=None):
                temp=temp.next
            temp.next=a[i].start

        self.sort()
        self.show()




    def sort(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                temp2=temp.next
                while temp2!=None:
                    if temp.data>temp2.data:
                        temp.data,temp2.data=temp2.data,temp.data
                    else:
                        pass
                    temp2=temp2.next
                temp=temp.next
            
        
    

a=ll()
b=ll()
d=ll()
#a object
a.insert(1)
a.insert(4)
a.insert(5)
#b object
b.insert(1)
b.insert(3)
b.insert(4)
#d object
d.insert(2)
d.insert(6)

b.merge((a,d))

