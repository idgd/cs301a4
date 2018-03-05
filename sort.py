# counting sort
# linear running time
# non-big-O: 2n + k, where k is the number of unique entries in the list
def sort_list(ulist):
	counted = dict((i,0) for i in ulist)
	for f in ulist:
		counted[f] += 1
	r = []
	for f in counted:
		r += [f] * counted[f]
	return(r)
