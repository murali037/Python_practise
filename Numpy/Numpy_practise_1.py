#%%
import numpy as np
#%%

# A 2 * 5 matrix
np_md_arr = np.array ( [
                        [1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10]
                        ] )

# Creates a 5 * 2 Matrix
# [ [1,2], [3,4], [5,6], [7,8], [9,10]]
np_modmd_arr = np_md_arr.reshape(5,2)

# A 1 * 4 Matrix
np_md_arr2 = np.array ( [1, 2, 3, 4] )

# Creates a 2 * 2 Matrix
#[ [1,2], [3,4] ]
np_modmd_arr2 = np_md_arr2.reshape(2,2)

#%%

np_nd_arr = np.arange(0,10)
# Generates => [0 1 2 3 4 5 6 7 8 9]
np_nd_arr = np.arange(0,10,2)
# Generates => [0 2 4 6 8] . The 3rd parameter '2' is step

# The step could be in floating point
np_nd_arr = np.arange(0,10,0.5)
# Generates => [ 0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]

# Generating n-dimension array from the output
np_nd_arr = np.arange(0,10).reshape(5,2)

np_nd_arr = np.arange(0,10,0.5).reshape(4,5)

#%% ones and zeros

np_array = np.zeros(10)
# Generates => [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
np_array = np.ones(10)
# Generates => [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
np_array = np.zeros((2,5))

np_array = np.ones((2,5))

# Changing the datatype as Integer
np_array = np.ones((2,5), dtype='Int32')

#%% compare size

py_arr = [1.1, 1.2,1.3424242, 1.436654646546, 454353.1232131, 32434353.324324, 1234.2321]
numpy_arr = np.array([1.1, 1.2,1.3424242, 1.436654646546, 454353.1232131, 32434353.324324, 1234.2321])

sizeof_py_arr = sys.getsizeof(12345.232343) * len(py_arr)           # Size  = 196
sizeof_numpy_arr = numpy_arr.itemsize * numpy_arr.size   # Size = 56

sizeof_py_arr
sizeof_numpy_arr



np_array = np.ones((2,5), dtype='Int32')
print(np_array)

np_array_size = np_array.itemsize * np_array.size
print(np_array_size)

np_array = np.ones((2,5), dtype='Int8')
print(np_array)

np_array_size = np_array.itemsize * np_array.size
print(np_array_size)

#%% comvert multidimenional array to single dimensional - ravel()

np_arr = np.arange(0,20).reshape(5, 4)

f_arr = np_arr.ravel()
# Generates = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(np_arr)
print(f_arr)

print(np_arr.shape)
print(f_arr.shape)

#%% lists vs numpy

list = [1,2,3]

print(list*2)

np_arr = np.array([1,2,3])

print(np_arr*2) # scalar multiplication

print(np_arr+2)

np_arr_t = np.transpose(np_arr)
print(np_arr.shape)
print(np_arr_t.shape)



#%%

arr1 = np.arange(4).reshape((2,2))
arr2 = np.arange(5,9).reshape((2,2))
print(arr1)
print(arr2)

# elementwise matrix multiplication
print(arr1*arr2)

# dot product
print(arr1.dot(arr2))

#%% mean, median, sum

print(arr1)
print(np.mean(arr1))
print(np.median(arr1))
print(np.sum(arr1))
print(np.min(arr1))
print(np.max(arr1))

#%% finding elements in an array
np_arr = np.array([0,1,2,3,4,5,56,8])
find = np.where(np_arr > 3)   # gives indices
print(find)
arr1
print(np.nonzero(np_arr))

print(arr1.shape)
print(np_arr.shape)
