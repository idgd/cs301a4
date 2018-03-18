from random import shuffle

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

def sort_list_radix(l):
	b = [[] for f in range(10)]
	d = 1
	m = True

	while m:
		m = False

		while l:
			t = l.pop()
			i = t // d
			b[i % 10].append(t)
			if i > 0:
				m = True

		for g in b:
			while g:
				l.append(g.pop())

		d *= 10
