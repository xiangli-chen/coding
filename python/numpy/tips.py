'''
general concepts
'''
# ndarray object is the core of NumPy - n-dimensional arrys of homogeneous data types
# NumPy arrays have a fixed size at creation
# Elements are all of the same data type

# ndarray object
import numpy as np

# Create arrays using array function from a Python list or tuple
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)])

# properties
a.ndim a.shape a.size a.dtype

np.zeros((3,4)) 
a.fill(0)
np.zeros(2,3,4) # row 3 col 4 depth 2
np.zeros_like(a) # an array of zeros with the same shape and type as a
np.ones((2,3), dtype = np.int16)
np.ones_like(a) # an array of ones with the same shape and type as a

np.arrange(10, 30, 5) # [10, 15, 20, 25]
np.linspace(0, 2, 5) # [0., 0.5, 1., 1.5, 2.]

# basic operations
# arithmetic operators on array apply elementwise
# product operate * operates elementwise in NumPy arrays
A*B # elementwise product
A.dot(B) np.dot(A, B) # matrix product

a = np.random.random((2, 3))
array([[ 0.47241611,  0.72747761,  0.43982429],
       [ 0.314428  ,  0.54312091,  0.48482687]])
a.sum() a.min() a.max() np.sum(a) np.min(a) np.max(a)
a.sum(axis=0) 
array([ 0.78684411,  1.27059851,  0.92465116])
a.min(axis=1) 
array([ 0.43982429,  0.314428])
b.cumsum(axis=1)

# Universal Functions
np.exp() np.sqrt() 
average ceil floor max min mean median round sort sum transpose trace


# Indexing, Slicing and Iterating
# One-dimensional
a[:6:2] = -1 # from start to positin 6 (exclude), set to -1
a[: :-1] # reversed a
# Multidimensional arrays
def f(x,y):
	return 10*x + y
b = np.fromfunction(f, (5,4), dtype = int)
b[i] = b[i,:] = b[i,...]

for row in b: # with respect to the first axis
for element in b.flat: # iterate over all the elements

# Shape Manipulation
a.ravel() # flatten the array
a.reshape(6, 2) np.reshape(a, (6, 2)) # returns a copy with a modified shape
a.shape = (6, 2) a.resize((2, 6)) # modify the array itself
a.T # Same as self.transpose(), except that self is returned if self.ndim < 2

# Stacking
np.vstack((a, b)) # vertical
np.hstack((a, b)) # horizontal
np.dstack((a, b)) # depth wise (along third axis)
np.concatenate(a, b, axis = 0 or 1 or ...) # for arrays of with more than two dimensions

# Splitting
np.hsplit(a, 2)
np.dsplit(a, 2)
np.split(a, axis = 0) # split a into 2

'''
Copies and Views
'''
a = np.arange(12)
b = a # two names for the same object
c = a.view() # different objects share the same data
d = a.copy() # copy method makes a complete copy of the array and its data

'''
Indexing and index tricks
'''
a = np.arrange(12)
index = np.array([1, 2, 3, 8, 5])
a[index]

a = np.arange(12).reshape(3, 4)
i = np.array([[0,1],[1,2]])
j = np.array([[2,1],[3,3]])
a[i,j]

a = np.arange(5)
a[[0,0,2]] = [1,2,3]