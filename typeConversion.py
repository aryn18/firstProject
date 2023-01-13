# implicit type
a = 10
b = 1.5
c = a+b
print(c)
d = True
e = a + d
print(e)

# explicit type
# example 1
s = "135"
i = 10 + int(s)
f = float(s)
print(i, f)

# example 2
s = "aryan"
print(list(s))
print(tuple(s))
print(set(s))

# example 3
l = ['a', 'b', 'c']

# if we print string with the list it shows sae output as we print the list in the
print(str(l))
a = 10
b = 11

# concatenation of a string
print(str(a) + str(b))
c = 12.5
print(str(c))

# example 4
t = (10, 20, 30)
print(list(t))
s = {10, 20 , 30}
print(list(s))

# example 5
a = 20
print(bin(a))
print(hex(a))
print(oct(a))

# example 6
a = "1001"
print(int(a, 2))
b = "12"
print(int(b, 8))
c = "A1"
print(int(c, 16))
