class ht:
	def __init__(self,l):
		# utility variable
		self.length = l
		# init to 0
		self.ht = [0]*l*4
		# constant time: initializes a couple variables

	def hashfunction(self,i):
		# modulo based hash
		return(i % self.length)
		# constant time: does one arithmetic operation

	def put(self,i):
		# where to put
		index = self.hashfunction(i)
		# if it's clear, put it in and return
		if self.ht[index] == 0:
			self.ht[index] = i
			return(True)
		else:
			# temp_index, because not indexing by default is the one thing I don't
			# like about python forloops
			temp_index = index
			# for each remaining slot after index
			for f in self.ht[index:]:
				# if there's a match
				if f == 0:
					self.ht[temp_index] = i
					return(True)
				# if there isn't one in the whole list
				elif len(self.ht[index:temp_index]) - len(self.ht[index:]) == -1:
					print("no empty slots - item not added")
					return(False)
				# increment index
				temp_index += 1
		# best case constant, worst case linear

	def contains(self,i):
		# where to look
		index = self.hashfunction(i)
		# if it's not there, iterate through list until it is or isn't found
		if self.ht[index] != i:
			for f in self.ht[index:]:
				if f == i:
					return(True)
				elif f == self.ht[-1]:
					print("item not found")
					return(False)
		# if it's there
		elif self.ht[index] == i:
			return(True)
		#best case constant, worst case linear

	def items(self):
		# return all items that have values in them
		return([f for f in self.ht if f != 0])
		# linear time: python forloops are linear

# to modify into a python dictionary:
"""
Use a non-colliding hash function, like sha2 or sha3, to generate the indices
Hash things as they come in, initialize with nothing
Because of non-collision, all the running times will be constant, as they will always be in best-case
"""
