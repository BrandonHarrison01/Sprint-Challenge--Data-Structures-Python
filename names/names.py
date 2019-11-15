import sys
from binary_search_tree import BinarySearchTree

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


tree = BinarySearchTree(names_1[0])
print(tree)
duplicates = []

for i in range(1, len(names_1)):
    tree.insert(names_1[i])

for j in range(0, len(names_2)):
    if tree.contains(names_2[j]) is True:
        duplicates.append(names_2[j])

# tree.in_order_print(tree)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

