import binary
import generate
import hashtable
import sort

sorted_list = generate.gen_list(1000)
unsorted_list = generate.gen_list_unsorted(1000)

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
