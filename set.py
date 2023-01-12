s1 = {10, 20, 30}
print(s1)

# if we pass any collection like list, tuple to make set we pass set constructor.
s2 = set([10, 20, 30])
print(s2)

# at line 9 we didn't create a empty set we create a dictionary.
s3 = {}
print(type(s3))

# at line 13 we create a empty with constructor
s4 = set()
print(type(s4))
print(s4)

# insertion operation
s5 = {10, 20}
s5.add(30)
print(s5)
# below two lines shows that if we add same value on set which is previously stored in set
# then it doesn't add into the set and this shows sets are distinct elements.
s5.add(30)
print(s5)

# update function will update the set or add new element in the set but order of the set is not fixed.
s5.update([40, 50])
print(s5)
s5.update({70, 60}, [80, 90])
print(s5)

# discard function work as it remove the element from the set and if we pass that
# value which is not present in set then it will run doesn't through any error.
s6 = {10, 20, 30, 40}
s6.discard(30)
print(s6)

# remove function also work as same as discard function but in remove function
# if we pass the element which is not present in the set it creates errors.
s6.remove(20)
print(s6)

# clear function clear all the element from the set. Doesn't delete the object of the set but delete the elements
s6.clear()
print(s6)

# add the element in an empty object.
s6.add(50)
print(s6)

# delete function delete the element of the set and also delete the object.
del s6

# len function printed the length of the set or total element in the set.
s7 = {10, 20, 30, 40}
print(len(s7))

# in operator work fast in sets in comparison to list because of sets working hashing internally.
print(20 in s7)
print(50 in s7)

s8 = {2, 4, 6, 8}
s9 = {3, 6, 9}

# | this parallel line used for union between two sets also we write s1.union(s2) or vice-versa.
print(s8 | s9)
print(s8.union(s9))

# and operator gives intersection of two sets or we represent with s1.intersection(s2) or vice-versa.
print(s8 & s9)
print(s8.intersection(s9))

# - operator gives the difference elements only present in set a or represent with s1.difference(s2) or vice-versa.
print(s8-s9)
print(s9.difference(s8))

# ^ operator gives the elements of both the sets but not the common elements
# or represent as s8.symmetric_difference(s9).
print(s8^s9)
print(s8.symmetric_difference(s9))

s10 = {2, 4, 6, 8}
s11 = {4, 8}

# isdisjoint gives us bool value true when both sets have no common value and false
# when both sets have different same value even one value is different.
print(s10.isdisjoint(s11))

# below operator called as subset operator and tells that set one is subset of set two or represent as s1.subset(a2).
print(s10 <= s11)

# below operator is a proper subset.
print(s10 < s11)

# below operator is super set is s1 is superset of s2 or represent wtih s1.issuperset(s2).
print(s10 >= s11)

# below operator is a proper super set is s1 is superset of s2.
print(s10 > s11)