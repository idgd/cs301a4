from random import shuffle

# silly bogosort (shuffles then checks against an already sorted list)
# this is just for fun :)
def sort_list_bogo(ulist):
	sorted_list = ulist[:]
	sorted_list.sort()
	shuffle(ulist)
	while ulist != sorted_list:
		shuffle(ulist)
	return(ulist)

# counting sort
# faster than python's built-in sort (timsort) at very large lists
# much, much more memory than timsort
# O(n)
def sort_list_counting(ulist):
	# find greatest and least values in the input list
	greatest = max(ulist)
	least = min(ulist)
	# create an ordered counting list
	count = [0 for f in range(least,greatest + 1)]
	# count each instance of a number in the input list
	for f in ulist:
		count[f] += 1
	# clear input list
	del ulist[:]
	iterator = 0
	# iterate over count
	while iterator < len(count):
		# create new list of counted variable
		new_piece = [i] * count[i]
		# extend the emptied list with this new list
		ulist.extend(new_piece)
		iterator += 1

# radix sort
# much slower than counting or timsort in implementation
# much less memory than counting sort (about 2n vs a lot more)
# O(n)
def sort_list_radix(ulist):
	# instantiate list of lists for all 10 digits
	buckets = [[] for f in range(10)]
	# which digit we are bucketing by
	digit = 1
	# logic switch
	loop = True

	while loop:
		# default the loop to end
		loop = False

		while ulist:
			# pop the end, remove the last n digits (by int division)
			temp = ulist.pop()
			index = temp // digit
			# dump into bucket by last digit (% 10)
			b[index % 10].append(temp)
			# if it's double digit, it's not done sorting
			if index > 0:
				loop = True

		# empty buckets back into list in order
		for g in buckets:
			while g:
				ulist.append(g.pop())

		# increment digit divisor to move to next digit
		digit *= 10
