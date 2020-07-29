class tree():
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

	def addt(self,data):
		if self.data:
			if data<self.data:
				if self.left is None:
					self.left=tree(data)
				else:
					self.left.addt(data)
			elif data>self.data:
				if self.right is None:
					self.right=tree(data)
				else:
					self.right.addt(data)
		else:
			self.data=data


	def show(self):
		if self.left:
			self.left.show()
		print(self.data)
		if self.right:
			self.right.show()



class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class ll:
	def __init__(self):
		self.start=None

	def add(self,data):
		if self.start is None:
			self.start=node(data)
		else:
			t=self.start
			while t.next!=None:
				t=t.next
			t.next=node(data)
	
	def show(self):
		if self.start is None:
			print("list is empty")
		else:
			t=self.start
			temp=tree(t.data)
			while t!=None:
				temp.addt(t.data)
				t=t.next
		temp.show()
		t=self.start
		while t!=None:
			print(t.data,end=' ')
			t=t.next








d=ll()
d.add(23)
d.add(34)
d.add(45)
d.add(5)
d.show()
