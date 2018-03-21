def bsearch(l,i):
	steps = 0
	# what's found
	found = None
	# halfway point, start, end
	h = int(len(l)/2)
	s = 0
	e = len(l) - 1
	while found != i:
		print(steps)
		steps += 1
		# found is the middle item
		found = l[int(round(h))]
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
