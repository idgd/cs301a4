class ht:
	def __init__(self,l):
		# support for 3 item overflow
		self.length = l
		self.ht = [0]*l*4
	def add(self,i):
		index = i % self.length
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
					return
				temp_index += 1
