class node:
	def __init__(self,value):
		self.data=value
		self.right=None
		self.left=None

class BST:
	def __init__(self):
		self.root=None


	def add(self,current,value):
		if self.root==None:
			self.root=node(value)
		else:
			if value<current.data:
				if current.left==None:
					current.left=node(value)
				else:
					self.add(current.left,value)

			else:
				if current.right==None:
					current.right=node(value)
				else:
					self.add(current.right,value)



	def visit(self):
		print(node.value)

	def preorder(self,current):
		self.visit(current)
		self.preorder(current.left)
		self.preorder(current.right)		



b=BST()
b.add(b,11)
b.add(b,9)
b.add(b,23)
b.add(b,5)
b.preorder(b)






