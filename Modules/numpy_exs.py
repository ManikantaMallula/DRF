# Importing NumPy and printing version number
#

import numpy as np
# print(np.__version__)

# Element-wise addition of 2 NumPy arrays
#
import numpy as np
# a = np.array([1,2,4])
# b = np.array([2,3,6])
# c = np.add(a,b)
# print(c)



# Multiplying a matrix (NumPy array) by a scalar

# a = 5
# b = [[1,2],[3,4]]
# print(np.dot(a,b))

# Identity Matrix

# a=np.identity(3)
# print(a)


# Array re-dimensioning

# n = np.array([1,2,3,4])
# print(n.shape, 'before')
#
# n.shape = (2,2)
# print(n.shape, 'after')


# Array datatype conversion
# a = np.array([1,2,3,4])
# print(a.dtype)
#
# b = a.astype('float64')
# print(b.dtype)

# c = a.astype('complex128')
# print(b.dtype)


# Obtaining Boolean Array from Binary Array

# a = np.array([True, False, True, True, False])
# b = a.astype(int)*255
# print(b)




# Horizontal Stacking of NumPy Arrays

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.hstack((a, b)))


# Vertically Stacking of NumPy Arrays

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack((a, b)))


# Custom Sequence Generation

# a = [x for x in range(1,10)]
# print(np.array(a))


# Getting the positions (indexes) where elements of 2 NumPy arrays match

# a = np.array([1, 2, 3])
# b = np.array([4, 2, 3])

# for i in a:
#     for j in b:
#         if i==j:
#             print(i,j)

# print(np.array(np.where(a==b)))  '''indexing position '''

# Generation of given count of equally spaced numbers within a specified range

print(np.linspace(0, 100, 10))
print(np.linspace(0, 100, 5))
print(np.linspace(0, 100, 2))



# Matrix Generation with one particular value
#
# Array Generation by repetition of a small array across each dimension
#
# Array Generation of random integers within a specified range
#
# Array Generation of random numbers
#
# Matrix Multiplication
#
# Matrix Transpose
#
# Sine of an Angle (in radians)
#
# Cosine Similarity
#
# Generating the array element indexes such that the array elements appear in ascending order