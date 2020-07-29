class Tree:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

	def add(self,data):
		if self.data:
			if data<self.data:
				if self.left is None:
					self.left=Tree(data)
				else:
					self.left.add(data)
			elif data>self.data:
				if self.right is None:
					self.right=Tree(data)
				else:
					self.right.add(data)
		else:
			self.data=data

	
	def show(self):
		if self.left:
			self.left.show()
		print(self.data)
		if self.right:
			self.right.show()
	
	
	def mindepth(self,i,j):
		if self.left:
			self.left.mindepth(i,j)
			i.append(1)	
			if self.right:
				self.right.mindepth(i,j)
				i.append(1)
		if self.right:
			self.right.mindepth(i,j)
			j.append(1)
			if self.left:
				self.left.mindepth(i,j)
				j.append(1)
		print(i,j)
		if sum(i)>sum(j):
			return i
		else:
			return j	

t=Tree(23)
t.add(12)
t.add(1)
t.add(43)
t.show()
d=t.mindepth([],[])
print("the minimum depth of Tree is",sum(d))