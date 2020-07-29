class Binary:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,value):
        if self.data:
            if value>self.data:
                if self.right==None:
                    self.right=Binary(value)
                else:
                    self.right.insert(value)
            elif value<self.data:
                if self.left==None:
                    self.left=Binary(value)
                else:
                    self.left.insert(value)

        else:
            self.data=data


    def depth1(self,dep=0,dep1=0):
        if self.left:
            dep+=1
            self.left.depth1(dep,dep1)
        if self.right:
            dep1+=1
            self.right.depth1(dep,dep1)
        print(dep,dep1)


a=Binary(9)
a.insert(3)
a.insert(20)
a.insert(15)
a.insert(10)
a.insert(40)
a.depth1()
