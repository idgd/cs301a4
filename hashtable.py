class ht:
	def __init__(self,l):
		# utility variable
		self.length = l
		# init to None
		self.ht = [None]*l*4
		# linear time: initializes a couple variables, multiplies list by k * 4

	def hashfunction(self,i):
		# modulo based hash
		return(i % self.length)
		# constant time: does one arithmetic operation

	def put(self,i):
		# where to put
		index = self.hashfunction(i)

		# if it's clear, put it in and return
		if self.ht[index] == None:
			self.ht[index] = i
			return(True)

		else:
			# for each remaining slot
			for f in self.ht:
				if f == None:
					self.ht.insert(self.ht.index(None),i)
					self.ht.remove(None)
					return(True)
				# increment index

			# if it's not found
			print("no empty slots - item not added")
			return(False)
		# best case constant, worst case linear

	def contains(self,i):
		# where to look
		index = self.hashfunction(i)
		# if it's not there, iterate through list until it is or isn't found
		if self.ht[index] != i:
			for f in self.ht:
				if f == i:
					return(True)
			print("item not found")
			return(False)
		# if it's there
		else:
			return(True)
		#best case constant, worst case linear

	def items(self):
		# return all items that have values in them
		return([f for f in self.ht if f != None])
		# linear time: python forloops are linear

# to modify into a python dictionary:
"""
Use a non-colliding hash function, like sha2 or sha3, to generate the indices
Hash things as they come in, initialize with nothing
Because of non-collision, all the running times will be constant, as they will always be in best-case
"""
