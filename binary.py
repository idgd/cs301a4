from generate import gen_list

### utility func

# finds the middle item
def half(l):
	return(l[int(len(l)/2)])

### binary search

def bsearch(l,i):
	print(l)
	found = None
	h = half(l)
	s = 0
	e = len(l) - 1
	while found != i:
		found = l[int(h)]
		print("half: " + str(int(h)) + ", Searching for: " + str(i))
		print(e - s, h)
		if i == found:
			return(True)
		elif e - s == 1:
			return(False)
		elif i < found:
			e = h
			h = (s + e)//2
		elif i > found:
			s = h
			h = (s + e)//2

# generate 1000 item list
l = gen_list(10)
# what to find
i = 5
print(bsearch(l,i))
