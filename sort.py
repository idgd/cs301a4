from random import shuffle
from generate import gen_list_unsorted as gen_list
from time import time

# silly bogosort (shuffles then checks against an already sorted list)
# this is just for fun :)
def sort_list_bogo(ulist):
	s = ulist[:]
	s.sort()
	shuffle(ulist)
	while ulist != s:
		print(ulist)
		shuffle(ulist)
	return(ulist)

# counting sort
# faster than python's built-in sort (timsort), but much more memory
def sort_list_counting(ulist):
	g = max(ulist)
	l = min(ulist)
	c = [0 for f in range(l,g + 1)]
	for f in ulist:
		c[f] += 1
	r = []
	i = 0
	while i < len(c):
		nl = [i] * c[i]
		r.extend(nl)
		i += 1
	return(r)
