# in python lists can be defined either through square brackets only or using a list class

# there can be any type of element in a single list

# 
print('\ncreate a list that contain all integers')

items = [1,2,3,4,5]

print('\nthis is the list containing all the integers: ', items)

# python lists can be appended using .append method
print('\nadd more elements to the list of undefined length')

for i in [12,13,14,15]:
    items.append(i)

print('\nappendded more integers to the list and now the new list is: ', items)


# try to append strings and float and repeated numbers to the same list

for i in ['one','two',1.5,3.2228]:
    items.append(i)

print('\nappendded strings and floats to the list and now the new list is: ', items)

for i in [1,1,1,2,3,5]:
    items.append(i)

print('\nthis is the final list and contains duplicate elements: ', items)

print('''\npython lists are immutable, means they can not be assigned like listA = listB. 
Assigning this way will just give another name to the same list.''')

listB = [1,2,3,4]
listA = listB

print('\n If we change a value in listA, the value will be changed in list B too because listA is just another name of the same list.')

listA[1]=12

print('\nchanged 2 to 12 at position 1 in listA, the change can be seen in both the lists')
print('list A: ', listA)
print('list B: ', listB)

print('\nlists can be coppied with .copy method')

listC = listA.copy()
print('\na copy of listA, ,list C: ', listC)

listC[3]=40

print('\nassigned 40 to position 3 in list C but it has not affected the listA, this can be seen\n')

print('list A: ', listA)
print('list C: ', listC)