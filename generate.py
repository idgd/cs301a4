from random import randint
#generate lists of n size

def gen_list(n):
	r = []
	for f in range(n):
		r.append(randint(0,f))
	r.sort()
	return(r)
