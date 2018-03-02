from generate import gen_list

### utility func

# splits list in half
def split(l,h):
	if len(l) == 1:
		return(l)

	half = int(len(l)/2)

	if h == 0:
		return(l[:half])
	else:
		return(l[half:])

# finds the middle item
def half(l):
	if len(l) == 1:
		return(l[0])
	return(l[int(len(l)/2)])

### binary search

# list, item
def bsearch(l,i):
	# stores candidate var
	found = None
	# while it's not the middle item
	while found != i:
		h = half(l)
		print("half: " + str(h) + ", Searching for: " + str(i))
		# if it's found
		if i == h:
			return(True)
		# if it's too short to split and not found
		elif len(l) == 1:
			return(False)
		# if it's probably in the last half
		elif i > h:
			l = split(l,1)
		# if it's probably in the first half
		elif i < h:
			l = split(l,0)

# generate 1000 item list
l = gen_list(1000)
# what to find
i = 500
print(bsearch(l,i))
