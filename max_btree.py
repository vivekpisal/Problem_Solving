import folium

class btree:
    max=0
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def insert(self,val):
        if self.data:
            if val>self.data:
                if self.right==None:
                    self.right=btree(val)
                else:
                    self.right.insert(val)
            elif val<self.data:
                if self.left==None:
                    self.left=btree(val)
                else:
                    self.left.insert(val)
        else:
            self.data=val



    def pbtree(self):
        if self.right:
            self.right.pbtree()
        print(self.data)
        if self.left:
            self.left.pbtree()



    def find_max(self):
        if self.left:
            self.left.find_max()
        if self.data>btree.max:
            btree.max=self.data
        if self.right:
            self.right.find_max()


    def printmax(self):
        self.find_max()
        print(btree.max)



a=btree(23)
a.insert(34)
a.insert(56)
a.insert(57)
a.insert(32)
a.insert(3)
a.insert(4)
a.insert(12)
a.printmax()   
