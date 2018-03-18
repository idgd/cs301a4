def bsearch(l,i):
	# what's found
	found = None
	# halfway point, start, end
	h = l[int(len(l)/2)]
	s = 0
	e = len(l) - 1
	while found != i:
		# found is the middle item
		found = l[int(h)]
		# if it's found
		if i == found:
			return(True)
		# if it's not (searchspace is size = 1 and it's not in there)
		elif e - s == 0:
			return(False)
		# if search item is less than the middle, go down
		elif i < found:
			e = h
			h = (s + e)/2
		# if search item is more than the middle, go up
		elif i > found:
			s = h
			h = (s + e)/2
