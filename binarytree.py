class node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

	
	def insert(self,value):
		if self.data:
			if value<self.data:
				if self.left is None:
					self.left=node(value)
				else:
					self.left.insert(value)
			elif self.data<value:
				if self.right is None:
					self.right=node(value)
				else:
					self.right.insert(value)
		else:
			self.data=value


	def tree(self):
		if self.left:
			self.left.tree()
		
		if self.right:
			self.right.tree()
		print(self.data)

	
	def search(self,ser):
		if self.data:
			#print('element is found')
			if self.data>ser:
				if self.left is None:
					print('element is not found')
				elif self.data ==ser:
					print('element is found')
				else:
					self.left.search(ser)
			elif self.data<ser:
				if self.right is None:
					print('element is not found')
				elif self.data ==ser:
					print('element is found')
				else:
					self.right.search(ser)



l=node(23)
l.insert(45)
l.insert(5)
l.insert(67)
l.insert(12)
l.tree()
l.search(67)

