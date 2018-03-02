# list, item
def bsearch(l,i):
	# stores candidate var
	found = None
	# while candidate is not correct and list is not cut too thin
	while found != i and len(l) != 1:
		# find the middle
		half = l[len(l)/2]
		# if it's in the last half, take the last half and try again
		if half > i:
			l = l[len(l)/2:]
			found = l[len(l)/2]
		# other half
		elif half < i:
			l = l[:len(l)/2]
			found = l[len(l)/2]
		# if it's been found
		else:
			return(True)
	# if it wasn't
	return(False)
