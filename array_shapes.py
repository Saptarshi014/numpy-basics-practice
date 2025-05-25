import numpy as np

# Reshaping arrays
array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape(2, 3)

print("Original Array:", array)
print("Reshaped Array:\n", reshaped_array)

# Transposing
transposed = reshaped_array.T
print("Transposed Array:\n", transposed)
