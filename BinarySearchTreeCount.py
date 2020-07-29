class node:
    count=0
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.dupli=0
        


    def insert(self,value):
        if self.data:
            if self.data<value:
                if self.right==None:
                    self.right=node(value)
                else:
                    self.right.insert(value)
            elif self.data>value:
                if self.left==None:
                    self.left=node(value)
                else:
                    self.left.insert(value)
            elif self.data==value:
                self.dupli+=1
        else:
            self.data=data



    def printT(self):
        if self.left:
            self.left.printT()
        print(self.data,self.dupli)
        node.count+=1
        if self.right:
            self.right.printT()



    @staticmethod
    def show():
        print(node.count)



a=node(23)
a.insert(34)
a.insert(45)
a.insert(45)
a.insert(34)
a.insert(12)
a.printT()
                
