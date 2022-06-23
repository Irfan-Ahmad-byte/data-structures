import array

# define an array with array built-in module, array type is fixed un this case i.e it can contain only same and defined type of elements
arr = array.array('i',[])
# the above list will include only integers
for i in range(6):
    arr.append(i)
print(arr)

# now, try to apend some string or float in the array
print('array.array with, try to append string into INT array')
for i in range(6):
    try:
        arr.append('one')
    except TypeError as e:
        print(e)
        
print('array.array with, try to append FLOAT into INT array')
for i in range(6):
    try:
        arr.append(1.0)
    except TypeError as e:
        print(e)

# following are the outputs
'''
array('i', [0, 1, 2, 3, 4, 5])
array.array with, try to append string into INT array
an integer is required (got type str)
an integer is required (got type str)
an integer is required (got type str)
an integer is required (got type str)
an integer is required (got type str)
an integer is required (got type str)
array.array with, try to append FLOAT into INT array
integer argument expected, got float
integer argument expected, got float
integer argument expected, got float
integer argument expected, got float
integer argument expected, got float
integer argument expected, got float
'''

# numpy arrays behave in a different manner
print('Now, trying numpy arrays')

import numpy as np

try:
    arr = np.array()
except Exception as e:
    print('This is numpy array creation without object error: ', e)
for i in range(6):
    try:
        arr.append(i)
    except Exception as e:
        print(e)
print(arr)

print('This gives an error because numpy array requires some object to create array and can not be aapended')

print('numpy.array with, try to append into numpy.array with python append')
arr = np.array([1,2,'one'])

for i in range(6):
    try:
        arr.append('one')
    except Exception as e:
        print(e)
print(arr)

print('numpy.array with, try to append FLOAT into INT array')
for i in range(6):
    try:
        arr.append(1.0)
    except Exception as e:
        print(e)
print(arr)

# numpy array with a defined array data type
print('************ Try to create an array of STRING and INT, but with a defined data type for the array.')
try:
    arr2 = np.array([1,2,3, 'one'], dtype='int')
except Exception  as e:
    print(e)

print('append into numpy.array using numpy.append')
print('array before appending: ',arr)
arr = np.array([1,2,'one'])
print('array after appending one: ',arr)
for i in range(6):
    try:
        np.append(arr, [['one']])
    except Exception as e:
        print(e)
print('array after appending two: ',arr)
for i in range(6):
    try:
        np.append(arr, [['two']])
    except Exception as e:
        print(e)
print('it can be noticed that numpy array stores only fixed length')