import numpy as np

def count_non_zero_numpy(arr):
  """Counts the number of non-zero elements in an array using NumPy."""
  numpy_array = np.array(arr)  # Convert the input to a NumPy array
  non_zero_count = np.count_nonzero(numpy_array) #use numpy count_nonzero function
  return non_zero_count

# Example usage:
my_array = [1, 0, 5, 0, -3, 2, 0]
non_zero_count = count_non_zero_numpy(my_array)
print(f"Number of non-zero elements: {non_zero_count}")

#Example with numpy arrays directly.
numpy_array_example = np.array([1, 0, 0, 4, 5, 0, -2])
non_zero_count_np = np.count_nonzero(numpy_array_example)
print(f"Number of non-zero elements(numpy array input): {non_zero_count_np}")