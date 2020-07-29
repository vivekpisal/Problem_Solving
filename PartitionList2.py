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
            while temp.next!=None:
                temp=temp.next
            temp.next=node(value)



    def show(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp.next!=None:
                print(temp.data,end='->')
                temp=temp.next
            print(temp.data)
            print()



    def partition(self,k):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            min1=[]
            max1=[]
            while(temp!=None):
                if temp.data>=k:
                    max1.append(temp.data)
                else:
                    min1.append(temp.data)
                temp=temp.next

            i=0
            j=0
            if self.start==None:
                    print("List is empty")
            else:
                temp=self.start
                while(temp!=None):
                    if i<len(min1):
                        temp.data=min1[i]
                        i+=1
                    elif j<len(max1):
                        temp.data=max1[j]
                        j+=1
                    temp=temp.next
        self.show()
                        
                
            
a=ll()
a.insert(1)
a.insert(4)
a.insert(3)
a.insert(2)
a.insert(5)
a.insert(90)
a.insert(2)
a.insert(8)
a.insert(12)
a.insert(45)
a.show()
a.partition(8)
