import numpy as np

# Define the arrays
a = np.array([1, 2, 3], dtype='int16')
print(a)

b = np.array([
    [9.0, 8.0, 7.0],
    [6.0, 5.0, 4.0]
])
print(b)

# Get dimension
print(a.ndim)
print(b.ndim)

# Get shape
print(a.shape)
print(b.shape)

# Get size (number of elements)
print(a.size)
print(b.size)

# Get type (dtype)
print(a.dtype)
print(b.dtype)

# Get itemsize (bytes per element)
print(a.itemsize)
print(b.itemsize)

# Get total size (bytes)
print(a.nbytes)
print(b.nbytes)