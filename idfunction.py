# id function gives us id of object not a variable.
# every object has different id
print(id(5))
a = 10
print(id(a))
b = a
print(id(b))
c = 20
d = 20
print(id(c), id(d))

# is method
x = 12
y = 12
print(x is y)

z = x
print(z is y)
z = 20
print(z is y)
