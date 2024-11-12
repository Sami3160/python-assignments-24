my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After append:", my_list)

my_list.extend([7, 8, 9])
print("After extend:", my_list)

my_list.insert(0, 0)
print("After insert:", my_list)

my_list.remove(0)
print("After remove:", my_list)

my_list.pop(0)
print("After pop:", my_list)

my_list.clear()
print("After clear:", my_list)

my_list = [1, 2, 3, 4, 5]

index = my_list.index(3)
print("Index of 3:", index)

count = my_list.count(3)
print("Count of 3:", count)

my_list.sort()
print("After sort:", my_list)

my_list.reverse()
print("After reverse:", my_list)

copy_list = my_list.copy()
print("Copy of the list:", copy_list)
