#%%
import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)

#%% slicing and dicing

a[:,2]
a[1,:]
a[0,:]

a[0, 0:6:2]

a[:,0]

a[:,0:10:2]

#%% 3-d example

b = np.array([[[1,2],[3,4]],[[3,5],[2,5]]])

print(b)

b[0,1,1]



#%% initializing different types of arrays

# all 0s matrix

x = np.zeros((2,3), dtype = 'int8')
print(x)

x = np.zeros((3,3,2), dtype = 'int8')
print(x)

# all 1s matrix

o = np.ones((2,3), dtype = 'int8')
print(o)

o = np.ones((3,3,2), dtype = 'int8')
print(o)

# any other number

n = np.full((3),3)
print(n)

n = np.full((2,3,3),3)
print(n)

# random numbers

# decimal
r = np.random.rand(2,2)
print(r)

# integer
r = np.random.randint(10,size=(2,2))  # random numbers from 0 to 10
print(r)

# identity matrix

print(np.identity(3,dtype='int8'))

#%%  Repeat elements

narr = np.array([[1,2],[3,4]])
print(narr)

#axis = 0  (repeat rows)
r1 = np.repeat(narr,3,0)
print(r1)

#axis = 1 (repeat columns)
r1 = np.repeat(narr,3,1)
print(r1)

#%%

exer = np.ones((5,5), dtype='int8')
print(exer)

exer[2,2] = 9
exer[1:4,1] = 0
exer[1:4,3] = 0
exer[1,2] = 0
exer[3,2] = 0

print(exer)


ones = np.ones((5,5), dtype='int8')
print(ones)

zeros = np.zeros((3,3), dtype='int8')
print(zeros)

ones[1:4,1:4] = zeros

ones[2,2] = 9

print(ones)


#%%  Be careful while copying arrays

a = np.array([1,2,3])

b=a

print(a)
print(b)

b[0]=100

print(a)
print(b)


#%% right way to copy

a = np.array([1,2,3])

b = a.copy()

print(a)
print(b)

b[0]=100

print(a)
print(b)

#%% Mathematics

x = np.array([1,2,3])
y = np.array([1,2,3])

print(x+2)
print(x-2)
print(x*2)
print(x/2)

print(x+y)
print(x-y)
print(x*y)
print(x/y)


print(x**2)

print(np.cos(x))
print(np.sin(x))
print(np.tan(x))

#%% Linear Algebra

x = np.full((2,3),1)   #2x3 matrix
y = np.full((3,2),2)   #3x2 matrix

print(x)
print(y)

# #columns should match #rows for dot product

print(x.dot(y))

print(np.matmul(x,y))

#%% find determinant
c = np.identity(3)
print(c)

print(np.linalg.det(c))

#%% Reorganize arrays

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)

print(a.reshape(1,6))

#%% vertical and horizontal stacking vectors

v1 = np.array([1,2,3,4,5])
v2 = np.array([11,12,13,14,15])

print(np.stack([[v1],[v1],[v2],[v2]]))

print(np.vstack([v1,v1,v2,v2]))

h1 = np.ones((2,2))
h2 = np.zeros((2,2))

print(np.hstack([h1,h2]))




