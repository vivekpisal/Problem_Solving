class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,value):
        if self.data:
            if value<self.data:
                if self.left==None:
                    self.left=Tree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right==None:
                    self.right=Tree(value)
                else:
                    self.right.insert(value)
        else:
            self.data=value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def search(self,val):
        if self.data==val:
            print(f"{self.data} found")
        else:
            if self.data:
                if val>self.data:
                    if self.right==None:
                        return f"{self.data} not found"
                    elif self.right.data==val:
                        return f"{self.data} found"
                    else:
                        return self.right.search(val)
                else:
                    if self.left==None:
                        return f"{self.data} not found"
                    elif self.left.data==val:
                        return f"{self.data} found"
                    else:
                        return self.left.search(val)
                

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    def preorder(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.preorder(root.left)
            res=res+self.preoreder(root.right)
        return res
            
    


a=Tree(23)
a.insert(34)
a.insert(45)
a.insert(12)
a.insert(11)
a.printTree()
