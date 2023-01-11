l = [10, 20, 30, 40, 50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])

# append function always add the element at the end of list.
l.append(12)
print(l)

# insert function add the element when we give the index it
# requires two parameters one is index and other is value or data.
l.insert(1, 23)
print(l)

# in method tells that any element or value is present in list or not. It shows bool value.
print(12 in l)

# count function gives us a number value how many times are coming in the list
print(l.count(30))

# index function gives us the index of that value.
print(l.index(30))

#  in line 26 we pass the range of index if 12 is present in between 4 and 7 indexes it gives the index of 12.
# starting index is inclusive which is 4 and end index is exclusive which is 7.
print(l.index(12, 4, 7))

li = [10, 20, 30, 40, 50, 60, 70, 80]
print(li)

# remove function remove the value or data from the list
li.remove(20)
print(li)

# pop function always remove or delete the element from the last or
# if we give the index then it will delete or remove the value from that given index.
print(li.pop())
print(li.pop(3))

# del keyword delete the value of the given index which we have passed
del li[1]
print(li)

# in del keyword we give the range of the indexes first index in inclusive and other is exclusive.
del li[0: 2]
print(li)

lis = [20, 30, 50, 90]

# max function shows the maximum value in the list.
print(max(lis))

# min function gives the minimum value of the function
print(min(lis))

# sum function gives the total of the list
print(sum(lis))

# reverse function give reverse index 0 is last index and last index is 0 index.
lis.reverse()
print(lis)

# sort function sorts the list in increasing order.
lis.sort()
print(lis)
