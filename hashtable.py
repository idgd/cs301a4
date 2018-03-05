class ht:
	def __init__(self,l):
		# support for 3 item overflow
		self.length = l
		self.ht = [0]*l*4

	def hashfunction(self,i):
		return(i % self.length)

	def put(self,i):
		index = self.hashfunction(i)
		if self.ht[index] == 0:
			self.ht[index] = i
		else:
			temp_index = index
			for f in self.ht[index:]:
				if f == 0:
					self.ht[temp_index] = i
					return
				elif len(self.ht[index:temp_index]) - len(self.ht[index:]) == -1:
					print("no empty slots - item not added")
					return(False)
				temp_index += 1

	def contains(self,i):
		index = self.hashfunction(i)
		if self.ht[index] != i:
			for f in self.ht[index:]:
				if f == i:
					return(True)
				elif f == self.ht[-1]:
					print("item not found")
					return(False)
		elif self.ht[index] == i:
			return(True)

	def items(self):
		return([f for f in self.ht if f != 0])
