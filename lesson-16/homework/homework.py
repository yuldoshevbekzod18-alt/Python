
#Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

#Expected Output:

#Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
import numpy as np

# Original list
original_list = [12.23, 13.32, 100, 36.32]
print("Original List:", original_list)

# Convert list to 1D numpy array
array_1d = np.array(original_list)

print("One-dimensional NumPy array:", array_1d)

#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#Expected Output:

#[[ 2 3 4] [ 5 6 7] [ 8 9 10]]
import numpy as np

# Create an array with values from 2 to 10 inclusive
values = np.arange(2, 11)  # 11 is exclusive, so 2 to 10

# Reshape into a 3x3 matrix
matrix = values.reshape((3, 3))

print(matrix)

#Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

#[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as np

# Create a null vector of size 10
null_vector = np.zeros(10)
print("Null vector:", null_vector)

# Update the sixth value (index 5) to 11
null_vector[5] = 11
print("Update sixth value to 11:", null_vector)

#Array from 12 to 38
#Write a NumPy program to create an array with values ranging from 12 to 38.

#Expected Output:

#[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np

# Create an array from 12 up to (but not including) 38
arr = np.arange(12, 38)

print(arr)

#Write a NumPy program to convert an array to a floating type.
#Sample output:
#Original array [1, 2, 3, 4]
import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)

# Convert to float type
float_array = original_array.astype(float)
print("Array converted to float:", float_array)

#Write a NumPy program to append values to the end of an array.
#Expected Output:
#Original array: [10, 20, 30]
#After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
import numpy as np

# Original array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Values to append
values_to_append = [40, 50, 60, 70, 80, 90]

# Append values
new_array = np.append(original_array, values_to_append)
print("After append values to the end of the array:", new_array)

#Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
import numpy as np

# Create a random array of 10 elements (values between 0 and 1)
random_array = np.random.rand(10)
print("Random array:", random_array)

# Calculate mean
mean_value = np.mean(random_array)

# Calculate median
median_value = np.median(random_array)

# Calculate standard deviation
std_dev = np.std(random_array)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev}")


#Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np

# Create a 10x10 array with random values between 0 and 1
random_array = np.random.rand(10, 10)
print("Random 10x10 array:\n", random_array)

# Find minimum value
min_value = np.min(random_array)

# Find maximum value
max_value = np.max(random_array)

print(f"\nMinimum value in the array: {min_value}")
print(f"Maximum value in the array: {max_value}")
