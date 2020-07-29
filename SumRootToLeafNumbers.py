class btree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


    def insert(self,val):
        if self.data:
            if self.data<val:
                if self.right==None:
                    self.right=btree(val)
                else:
                    self.right.insert(val)
            elif self.data>val:
                if self.left==None:
                    self.left=btree(val)
                else:
                    self.left.insert(val)
        else:
            self.data=data



    def show(self):
        if self.right:
            self.right.show()
        print(self.data)
        if self.left:
            self.left.show()
            

    def sumroot(self,sum1=[],temp1=[]):
        if self.right:
            temp1.append(self.data)
            self.right.sumroot(sum1,temp1)
            print(sum1,temp1)
        elif self.left:
            temp1.append(self.data)
            self.left.sumroot(sum1,temp1)
            print(sum1,temp1)
        

a=btree(2)
a.insert(1)
a.insert(3)
a.sumroot()
