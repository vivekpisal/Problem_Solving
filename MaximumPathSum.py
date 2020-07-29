class node:
    sum=0
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



    def  insert(self,value):
        if self.data:
            if self.data>value:
                if self.right==None:
                    self.right=node(value)
                else:
                    self.right.insert(value)
            else:
                if self.data<value:
                    if self.left==None:
                        self.left=node(value)
                    else:
                        self.left.insert(value)
        else:
            self.data=data



    def show(self):
        if self.left:
            self.left.show()
        node.sum+=self.data
        print(self.data)
        if self.right:
            self.right.show()


            
    @classmethod
    def Maxsum(cls):
        print("Max Sum:",cls.sum)




a=node(7)
a.insert(3)
a.insert(4)
a.insert(10)
a.show()
a.Maxsum()
