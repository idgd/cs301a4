from time import time as t

import binary
import generate
import hashtable
import sort

print("Hashtable test")
hashtable = hashtable.ht(5)
hashtable.put(5)
hashtable.put(5)
hashtable.put(5)
hashtable.put(5)
hashtable.put(4)
hashtable.put(3)
hashtable.put(2)
hashtable.put(1)
print(hashtable.contains(5))
print(hashtable.contains(50))
print(hashtable.items())

print("\nBinary Search test")

sorted_list = [f for f in range(257)]

print(binary.bsearch(sorted_list,0))
print(binary.bsearch(sorted_list,64))
print(binary.bsearch(sorted_list,128))
print(binary.bsearch(sorted_list,256))
print(binary.bsearch(sorted_list,512))

print("\nSorting test")

print("Correctness")
unsorted_list = [123,32,46,98,88,334,523,32,32,16]
print("Unsorted list: ", unsorted_list, "\nCounting Sort")
sort.sort_list_counting(unsorted_list)

print(unsorted_list, "\nRadix Sort")
unsorted_list = [123,32,46,98,88,334,523,32,32,16]
sort.sort_list_radix(unsorted_list)

print(unsorted_list, "\nQuick Sort")
unsorted_list = [123,32,46,98,88,334,523,32,32,16]
sort.sort_list_quick(unsorted_list)
print(unsorted_list)

print("\nTimes")

unsorted_list = generate.gen_list_unsorted(1048576)

s_counting = t()
sort.sort_list_counting(unsorted_list)
e_counting = t()
print("Counting sort time: " + str(e_counting - s_counting))

unsorted_list = generate.gen_list_unsorted(1048576)

s_radix = t()
sort.sort_list_radix(unsorted_list)
e_radix = t()
print("Radix sort time: " + str(e_radix - s_radix))

unsorted_list = generate.gen_list_unsorted(1048576)

s_quick = t()
sort.sort_list_quick(unsorted_list)
e_quick = t()
print("Quicksort sort time: " + str(e_quick - s_quick))

unsorted_list = generate.gen_list_unsorted(1048576)

s_tim = t()
unsorted_list.sort()
e_tim = t()
print("Timsort sort time: " + str(e_tim - s_tim))
