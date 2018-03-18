from random import randint
#generate lists of n size

def gen_list(n):
	r = []
	for f in range(n):
		r.append(randint(0,n))
	r.sort()
	return(r)

def gen_list_unsorted(n):
	r = []
	for f in range(n):
		r.append(randint(0,n))
	return(r)
