age = 21
name = "Aryan"
weight = 80
print(age)
print(name)
print(weight)

price = 100
tax = 18
totalPrice = price + tax
print(totalPrice)

# How variable work
""" When we create a variable let suppose x one memory location is created 
and this memory location stores the data of x when we call x and this value 
is called out from memory and x is reference for that memory block. """
x = 10
y = "python"
z = 20
w = z
# in line 20 we create a variable w and set value z
# in this case w become one more reference of that
# memory location in which y value is stored
w = 30
# in line 24 we assign the value to w which is 30 now onwards w is reference a new memory block in which 30 is stored
print(x, y, z, w)

# python is dynamically typed because variables are just reference
# to memory location they don't have any type information association with that.
x = 21
print(x)
x = "ary"
print(x)
