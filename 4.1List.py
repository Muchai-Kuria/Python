name = ["Lee", "Muchai", "Kuria","Peter","Charles","Collins"]

print(name)
print(len(name))
print(name[1])

#Slicing
print(name[0:3])# Print in between index 0 and 3 but 3.
print(name[4:6])
print(name[3:])

#Modifying
name[0] = "John"#Changing index 0
name.append("Michael")
name.insert(0,"Jane")

name_2 = ["Julia","Agnes"]
name.extend(name_2)

print(name)

#Removing items

name.remove("Muchai")
name.pop() # Removes the last item
name.reverse()
name.sort()
print(name)

#Printing a list
for i in enumerate(name, start=1):
    print(i)

#joining a list
name_join = " - ".join(name)# - can change its just a joiner
print(name_join)

#Spliting a list
name_split = name_join.split(" - ")
print(name_split)