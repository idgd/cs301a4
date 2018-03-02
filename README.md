# cs301a4
CS 301 Searching Lists

# Deliverable 1
~~Implement a binary search on a sorted list.~~ - DONE

# Deliverable 2
Implement a hash table.

* Create an empty list that's much larger than the expected number of items
* Create a hash function that gives an index for that item.
* Implement collision solving (move it to next empty slot)
* Search by hashing, which gives us the slot the value should be in. If the slot is empty, it doesn't exist. If it has another value in it, search up the list until it matches or the list ends, in which case it doesn't exist.

This will be implemented using a `HashList` class. Inputs will be integers.

* `HashList(lengeth)` - Creates a new empty `HashList` of the given length
* `hashfunction(item)` - Gives the slot an item should go into
* `put(item)` - Adds item to list; if full, throw error
* `contains(item)` - Returns true if thel given item exists, false otherwise
* `items()` - Returns all items

# Deliverable 3

Explain and justify running times in the `HashList` methods, using best and worst case scenarios.

# Deliverable 4

Explain how to modify the `HashList` class to match a dictionary.

# Deliverable 5

Implement a `sort_list(ulist)` function that sorts the given list using any method.
