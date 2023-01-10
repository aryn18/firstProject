x = "Python"
y = "Repo"

# method 1
temp = x
x = y
y = temp
print(x)
print(y)

# method 2
x, y = y, x
print(x)
print(y)

# assigning variable with comma in a single line
a, b, c = 100, "python", 20.4
print(a)
print(b)
print(c)

a, b = a - 10, b + " coder"
print(a)
print(b)
