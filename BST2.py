class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def insert(self,value):
        if self.data:
            if self.data>value:
                if self.right==None:
                    self.right=node(value)
                else:
                    self.right.insert(value)
                    
            elif self.data<value:
                if self.left==None:
                    self.left=node(value)
                else:
                    self.left.insert(value)
        else:
            self.data=value

    def printB(self):
        if self.left:
            self.left.printB()
        print(self.data)
        if self.right:
            self.right.printB()

a=node(23)
a.insert(35)
a.insert(545)
a.insert(67)
a.insert(2)
a.printB()
