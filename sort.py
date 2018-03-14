from random import shuffle
from generate import gen_list_unsorted as gen_list
from time import time as t
from math import log10

def msd(i):
	if i == 0:
		return((0,0))

	e = int(log10(i))
	r = int(i/10**e)
	return((r,e))

def sd(i,d):
	if i == 0:
		return(0)

	e = int(log10(i))
	r = int(i/10**e)
	i -= r * 10**e
	if e + 1 > d:
		sd(i,d)
	return(r)

print(sd(256234,1))

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
# faster than python's built-in sort (timsort) at very large lists
# much, much more memory than timsort
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

# radix sort
def sort_list_radix(ulist):
	l = max([msd(f)[1] for f in ulist])
	while l >= 0:
		b = [list() for f in range(10)]
		for f in ulist:
			m = msd(f)
			b[m[0]].append(f)
		b = [item for sublist in b for item in sublist]
		l -= 1

m = gen_list(10)
sort_list_radix(m)
