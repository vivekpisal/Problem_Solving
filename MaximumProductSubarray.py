class btree:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

	def insert(self,data):
		if self.data:
			if self.data>data:
				if self.left==None:
					self.left=btree(data)
				else:
					self.left.insert(data)
			else:
				if self.right==None:
					self.right=btree(data)
				else:
					self.right.insert(data)
		else:
			self.data=data


	def show(self):
		if self.right:
			self.right.show()
		print(self.data)
		if self.left:
			self.left.show()


a=btree(23)
a.insert(34)
a.insert(56)
a.insert(5)
a.show()



		
