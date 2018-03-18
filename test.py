from time import time as t

import binary
import generate
import hashtable
import sort

sorted_list = [f for f in range(257)]
unsorted_list = generate.gen_list_unsorted(1048576)

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
print(binary.bsearch(sorted_list,0))
print("")
print(binary.bsearch(sorted_list,64))
print("")
print(binary.bsearch(sorted_list,128))
print("")
print(binary.bsearch(sorted_list,256))
print("")
print(binary.bsearch(sorted_list,512))

print("\nSorting test")

s_counting = t()
sort.sort_list_counting(unsorted_list)
e_counting = t()
print(e_counting - s_counting)

s_tim = t()
unsorted_list.sort()
e_tim = t()
print(e_tim - s_tim)
