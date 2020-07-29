class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


    def insert(self,data):
        if self.data:
            if data>self.data:
                if self.right is None:
                    self.data=data
                else:
                    self.right.insert(data)
            elif data<self.data:
                if self.left is None:
                    self.data=data
                else:
                    self.left.insert(data)
        else:
            self.data=data


    def view(self):
        if self.left:
            self.left.view()
        print(self.data)
        if self.right:
            self.right.view()


a=node(23)
a.insert(5)
a.insert(34)
a.insert(45)
a.insert(56)
a.view()
                
                    
