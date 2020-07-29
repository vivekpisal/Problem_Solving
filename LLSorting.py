class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class ll:
    c=[]
    def __init__(self):
        self.start=None


    def add(self,data):
        if self.start==None:
            self.start=node(data)
            ll.c.append(data)
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
            ll.c.append(data)



    def show(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()



    def ll_sort(self):
        if self.start==None:
            print("List is empty")
        else:
            ll.c.sort()
            i=0
            temp=self.start
            while temp!=None:
                temp.data=ll.c[i]
                temp=temp.next
                i+=1
            self.show()
            
                

a=ll()
a.add(23)
a.add(78)
a.add(56)
a.show()
a.ll_sort()
