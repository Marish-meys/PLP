# This is a Python script that demonstrates the use of lists and their methods.
# It creates a list of integers, modifies it by adding, removing, and sorting elements,
my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.append(6)       
my_list.append(7)
my_list.append(8)   
my_list.append(9)
my_list.append(10)
my_list.append(11)
my_list.append(12)
my_list.append(13)

my_list.insert(2,20)

my_list.extend([14, 15, 16, 17, 18, 19])
my_list.remove(2)
my_list.pop(5)
my_list.sort()
my_list.reverse()
my_list.clear()
# Find and print the index of the value 4 in the list
print("Index of 4:", my_list.index(4) if 4 in my_list else "Not found")
# and prints the final list.
# It also demonstrates the use of the index method to find the position of a specific value.
# The script is a simple demonstration of list operations in Python.                                    

