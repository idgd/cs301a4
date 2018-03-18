### utility func

# finds the middle item
def half(l):
	return(l[int(len(l)/2)])

### binary search

def bsearch(l,i):
	# testing found edgecase: won't find first/last items
	if l[0] == i or l[-1] == i:
		return(True)

	# what's found
	found = None
	# halfway point, start, end
	h = half(l)
	s = 0
	e = len(l) - 1
	while found != i:
		# found is the middle item
		found = l[int(h)]
		# print where it's at
		print("half: " + str(int(h)) + ", Searching for: " + str(i))
		# if it's found
		if i == found:
			return(True)
		# if it's not (searchspace is size = 1 and it's not in there)
		elif e - s == 1:
			return(False)
		# if search item is less than the middle, go down
		elif i < found:
			e = h
			h = (s + e)//2
		# if search item is more than the middle, go up
		elif i > found:
			s = h
			h = (s + e)//2
