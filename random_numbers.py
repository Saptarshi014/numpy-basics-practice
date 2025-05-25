import numpy as np

# Generating random numbers
random_array = np.random.rand(3, 3)  # 3x3 matrix with values between 0 and 1
print("Random Array:\n", random_array)

# Random integers
random_integers = np.random.randint(
    1, 10, size=(3, 3)
)  # 3x3 matrix of random ints between 1 and 10
print("Random Integers:\n", random_integers)

# Setting a seed for reproducibility
np.random.seed(42)
print("Random Array with Seed:\n", np.random.rand(3, 3))

# Shuffling an array
