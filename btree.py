class btree:
    sum1=0
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

    def  insert(self,value):
        if self.data:
            if self.data>value:
                if self.right==None:
                    self.right=btree(value)
                else:
                    self.right.insert(value)
            elif self.data<value:
                if self.left==None:
                    self.left=btree(value)
                else:
                    self.left.insert(value)
        else:
            self.data=value


    def show(self):
        if self.right:
            self.right.show()
        print(self.data)
        sum1+=self.data
        if self.left:
            self.left.show()
        


a=btree(2)
a.insert(23)
a.insert(34)
a.insert(45)
a.insert(56)
a.show()
