t = (10, 20, "python")
print(t)
print(type(t))

# this is empty tuple
tu = ()
print(tu)
print(type(tu))

# this always gives integer value or if pass string value then it gives string value.
tup = (10)
print(tup)
print(type(tup))

# this shows the tuple creation.
tupl = (10, )
print(type(tupl))

tuple = 10, 20, 30, 40, 10
print(tuple)

# this shows the value at index 2
print(tuple[2])

# this shows the value at index -1
print(tuple[-1])

# this shows the value in between 1 and 3 inclusive at index and exclusive at index 3.
print(tuple[1:3])

# this print the length of the tuple
print(len(tuple))

# this print the 1st present value in the given tuple
print(tuple.count(10))

# this shows the index of the given value.
print(t.index(20))
