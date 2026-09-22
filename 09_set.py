# set is a collection of non-repitative elements. 
# It is unordered and unindexed.
# In Python, sets are written with curly brackets.

empty_set = set() # empty set
s={1,3,5,7,3,4,3,9,6,5,4,3,"mahak",2}
print(s)
s.add(23)
print(s)
s.remove(3)
print(s)
s.discard(3) # removes an element from the set if it is a member. If not a member, do nothing.
print(s)
s.pop() # removes a random element from the set
print(s)

s1={1,2,3,4,5}
s2={1,2,3,4}
print(s1.union(s2)) # returns a set containing all items from both sets, duplicates are excluded
print(s1.intersection(s2)) # returns a set containing only items that are present in both sets  
print(s1.difference(s2)) # returns a set containing items that are present in the first set but not in the second set.
print(s1.issubset(s2))
print(s1.issuperset(s2))