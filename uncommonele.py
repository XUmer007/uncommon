list1 = [1, 2, 3, 4, 5, 6, 123]
list2 = [3, 4, 5, 6, 7, 8, '123']

list1_str = [str(x) for x in list1]
list2_str = [str(x) for x in list2]

uncommon_elements = []

for i in list1_str:
    if i not in list2_str:
        uncommon_elements.append(i)


for j in list2_str:
    if j not in list1_str:
        uncommon_elements.append(j)

print("list1:", list1)
print("list2:", list2)
print("Uncommon elements from the lists:", uncommon_elements)
