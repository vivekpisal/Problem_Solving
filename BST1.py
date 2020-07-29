class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=self.data


    def printtree(self):
        if self.right:
            self.right.printtree()
        print(self.data)
        if self.left:
            self.left.printtree()

# Use the insert method to add nodes
root = node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printtree()
















            
            
