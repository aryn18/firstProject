d = {110: "xyz", 101: "abc", 105: "bcd", 104: "abc"}
print(d)

# empty dictionary
d1 = {}
print(d1)

# we add item in dictionary as follows also
dic = {}
dic["laptop"] = 40000
dic["mobile"] = 20000
dic["earphone"] = 1000
print(dic)

# key work as index also in dictionary
print(dic["mobile"])

d2 = {11: "ab", 12: "cd", 13: "ef"}

# this gives a value stored in a passing key.
print(d2.get(11))

# if the key is not present in the dictionary then it shows the value as none
print(d2.get(14))

# a for loop for finding the value of passing key
if 14 in d2:
    print(d[14])
else:
    print("No value associated with it.")

# a simpler method without using for loop.
print(d.get(14, "No value associated with it."))

d3 = {21: "ab", 22: "cd", 23: "ef", 24: "gh"}
print(d3)

# this update the value 23 key from ef to ij
d3[23] = "ij"
print(d3)

# len function gives the total pair in the dictionary
print(len(d3))

# pop function delete the element an shows the value in the console
print(d3.pop(22))

# del function delete the key and value but didn't show delete pair in the console.
del d3[23]
print(d3)

# it adds the pair in the last in the dictionary.
d3[25] = "mn"
print(d3)

# it deletes the pair from the end of the dictionary and showing delete pair in the console.
print(d3.popitem())
